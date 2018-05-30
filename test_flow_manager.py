import unittest
import flow_manager
from Switch import Flow

TEST_SERVER = "robustsfc.pl.sophia.inria.fr"


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(True, True)

    def test_add_flow_1(self):
        es = flow_manager.ExtendedSwitch("openflow:1", TEST_SERVER)
        es.add_flow(table_id="0", flow=Flow("0"))

    def test_add_flow_2(self):
        es = flow_manager.ExtendedSwitch("openflow:1", TEST_SERVER)
        es.add_flow(table_id="0", flow=Flow("0", priority="666", ipv4="10.0.0.0/24"))

    def test_remove_flow_1(self):
        es = flow_manager.ExtendedSwitch("openflow:1", TEST_SERVER)
        es.add_flow(table_id="0", flow=Flow("0"))
        es.remove_flow("0", "0")

    def test_remove_flow_2(self):
        es = flow_manager.ExtendedSwitch("openflow:1", TEST_SERVER)
        es.add_flow(table_id="0", flow=Flow("0"))
        try:
            es.remove_flow(table_id="1", flow_id="0")
        except KeyError:
            es.remove_flow(table_id="0", flow_id="0")
            self.assertTrue(True)

    def test_remove_flow_3(self):
        es = flow_manager.ExtendedSwitch("openflow:1", TEST_SERVER)
        es.add_flow(table_id="0", flow=Flow("0"))
        try:
            es.remove_flow(table_id="0", flow_id="1")
        except KeyError:
            es.remove_flow(table_id="0", flow_id="0")
            self.assertTrue(True)

    def test_get_flows(self):
        es = flow_manager.ExtendedSwitch("openflow:1", TEST_SERVER)
        response = es.get_flows()
        self.assertIn("node", response)




if __name__ == '__main__':
    unittest.main()
