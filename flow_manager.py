import ODL_client as Controller_client

import Switch

class flow_manager(object):
    def __init__(self, network, Controller_address, port="8181", user="admin", password="admin"):
        client = Controller_client.Client(Controller_address, port, user, password)

