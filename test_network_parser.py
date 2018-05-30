import unittest
import network_parser

DUMMY_PATH = "dummy_file.txt"


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(True, True)

    def test__NetworkParser_1(self):
        np = network_parser.NetworkParser(DUMMY_PATH)
        self.assertEqual({("1", "2"), ("2", "3")}, np.links)

    def test__NetworkParser_2(self):
        np = network_parser.NetworkParser(DUMMY_PATH)
        self.assertEqual({"1", "2", "3"}, np.switches)

    def test_create_network_1(self):
        np = network_parser.NetworkParser(DUMMY_PATH)
        network = np.create_network()
        self.assertAlmostEqual(3, len(network.keys()))

    def test_create_network_2(self):
        np = network_parser.NetworkParser(DUMMY_PATH)
        network = np.create_network()
        self.assertTrue(network["1"].check_link("1", "2"))

    def test_create_network_3(self):
        np = network_parser.NetworkParser(DUMMY_PATH)
        network = np.create_network()
        self.assertTrue(network["2"].check_link("1", "2"))

    def test_create_network_4(self):
        np = network_parser.NetworkParser(DUMMY_PATH)
        network = np.create_network()
        self.assertTrue(network["1"].check_link("2", "1"))

    def test_create_network_5(self):
        np = network_parser.NetworkParser(DUMMY_PATH)
        network = np.create_network()
        self.assertFalse(network["1"].check_link("2", "3"))

    def test_create_network_6(self):
        np = network_parser.NetworkParser(DUMMY_PATH)
        network = np.create_network()
        self.assertTrue(network["3"].check_link("3", "2"))

if __name__ == '__main__':
    unittest.main()
