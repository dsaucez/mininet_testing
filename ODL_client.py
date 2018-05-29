import requests
import json

class Client(object):

    def __init__(self, address, port="8181", user="admin", password="admin"):
        self.address = address
        self.user = user
        self.password = password
        self.port = port
        self.header = {"Accept": "*/*", "Cache-Control": "no-cache", "Content-Type": "application/yang.data+json"}

    def get_flows(self, switch):
        switch = str(switch)

        link = "http://{}:{}/restconf/config/opendaylight-inventory:nodes/node/{}".format(self.address, self.port, switch)
        response = requests.get(link, auth=(self.user, self.password))
        data = response.json()
        return data

    def add_flow(self, switch, table="0", id="1", priority="1", flow_name = "None", ipv4=None, instruction=None):
        switch, table, id, priority, flow_name = str(switch), str(table), str(id), str(priority), str(flow_name)

        link = "http://{}:{}/restconf/config/opendaylight-inventory:nodes/node/{}/flow-node-inventory:table/{}/flow/{}"\
            .format(self.address, self.port, switch, table, id)
        payload = {
                "flow": {
                    "priority": priority,
                    "flow-name": flow_name,
                    "id": id,
                    "table_id": table
                }
            }

        if ipv4:
            payload["flow"]["match"] = {
                        "ethernet-match": {
                            "ethernet-type": {
                                "type": "2048"
                            }
                        },
                        "ipv4-destination": ipv4
                    }

        if instruction:
            payload["flow"]["instructions"] = {
                "instruction": instruction
                }
        response = requests.put(link, json.dumps(payload), auth=(self.user, self.password), headers=self.header)
        return response


    def remove_flow(self,switch, table, id):
        switch, table, id = str(switch), str(table), str(id)
        link = "http://{}:{}/restconf/config/opendaylight-inventory:nodes/node/{}/flow-node-inventory:table/{}/flow/{}"\
            .format(self.address, self.port, switch, table, id)
        print(link)
        response = requests.delete(link, auth=(self.user, self.password), headers=self.header)
        return response


