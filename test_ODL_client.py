import unittest
import ODL_client as ODL
import requests


ODL_SERVER = "robustsfc.pl.sophia.inria.fr"


class ODLTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(True, True)

    def test_create_client(self):
        ODL.Client(ODL_SERVER)

    def test_add_flow_dummy(self):
        c = ODL.Client(ODL_SERVER)
        response = c.add_flow(switch="openflow:1", table="0", id="0",priority="666", ipv4="10.0.0.0/24")
        self.assertTrue(response.status_code == 200 or response.status_code == 201)

    def test_remove_flow(self):
        c = ODL.Client(ODL_SERVER)
        response = c.remove_flow(switch="openflow:1", table="0", id="0")
        self.assertEqual(response.status_code, 200)

    def test_get_flows(self):
        c = ODL.Client(ODL_SERVER)
        response = c.get_flows("openflow:1")
        self.assertIn("node", response)


if __name__ == '__main__':
    unittest.main()
