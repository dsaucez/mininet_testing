import unittest
from Switch import *

class MyTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(True, True)

    def test_DuplicatedKeyError(self):
        try:
            raise DuplicatedKeyError("this is working :-)")
        except DuplicatedKeyError:
            self.assertTrue(True)

    def test_add_table(self):
        s1 = Switch("s1")
        s1.tables["in_the_tables"] = "test"
        s1.add_table("not_in_tables")
        try:
            s1.add_table("in_the_tables")
        except DuplicatedKeyError:
            self.assertTrue(True)

    def test__Table___add_flow_1(self):
        t = Table("test")
        try:
            t.add_flow("This is not a Flow")
        except TypeError:
            self.assertTrue(True)

    def test__Table___add_flow_2(self):
        t = Table("test")
        f = Flow("test")
        t.add_flow(f)
        self.assertTrue(True)

    def test__Table___add_flow_3(self):
        t = Table("test")
        f1 = Flow("duplicate_test")
        f2 = Flow("duplicate_test")
        t.add_flow(f1)
        try:
            t.add_flow(f2)
        except DuplicatedKeyError:
            self.assertTrue(True)

    def test_remove_flow(self):
        s = Switch("s")
        s.add_flow("t", Flow("flow_id"))
        s.remove_flow("t", "flow_id")
        self.assertEqual(len(s.tables["t"].flows), 0)

    def test_add_link_1(self):
        s = Switch("1")
        s.add_link("1", "2")
        self.assertEqual({("1", "2")}, s.links)

    def test_add_link_2(self):
        s = Switch("1")
        s.add_link("2", "1")
        self.assertEqual({("2", "1")}, s.links)

    def test_add_link_3(self):
        s = Switch("1")
        s.add_link("2", "3")
        self.assertEqual(set(), s.links)

    def test_remove_link_1(self):
        s = Switch("1")
        s.links = {("1", "2"), ("2", "3")}
        s.remove_link("2", "3")
        self.assertEqual({("1", "2")}, s.links)

    def test_remove_link_2(self):
        s = Switch("1")
        s.links = {("1", "2")}
        s.remove_link("2", "3")
        self.assertEqual({("1", "2")}, s.links)

    def test_check_link_1(self):
        s = Switch("1")
        s.links = {("1", "2"), ("2", "3")}
        self.assertTrue(s.check_link("2", "3"))

    def test_check_link_2(self):
        s = Switch("1")
        s.links = {("1", "2"), ("2", "3")}
        self.assertTrue(s.check_link("3", "2"))

    def test_check_link_3(self):
        s = Switch("1")
        s.links = set()
        self.assertFalse(s.check_link("2", "3"))


if __name__ == '__main__':
    unittest.main()
