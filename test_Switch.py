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
        s.tables["t"] = {"flow_id": "666"}
        s.remove_flow("t", "flow_id")
        self.assertEqual(len(s.tables["t"]), 0)



if __name__ == '__main__':
    unittest.main()
