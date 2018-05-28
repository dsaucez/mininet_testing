import unittest
import ODL_client as ODL
import requests

class ODLTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(True, True)

    def test_create_client(self):
        ODL.Client("localhost")

    def test_get_flows(self):
        c = ODL.Client("127.0.0.1")
        c.get_flows("openflow:1")

    def test_add_flow_dummy(self):
        c = ODL.Client("robustsfc.pl.sophia.inria.fr")
        response = c.add_flow(switch="openflow:1")
        print(response.content)


if __name__ == '__main__':
    unittest.main()
