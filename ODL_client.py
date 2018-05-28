import requests
import json

class Client(object):

    def __init__(self, address, port="8181", user= "admin", password= "admin"):
        self.address = address
        self.user = user
        self.password = password
        self.port = port

    def get_flows(self, switch):
        link = "http://{}:{}/restconf/config/opendaylight-inventory:nodes/node/{}".format(self.address, self.port, switch)
        response = requests.get(link, auth=(self.user, self.password))
        data = response.json()
        return data

    def add_flow(self, switch, table="0", id="1", priority="1", flow_name = "No_Name", ip=None, instruction=None):
        link = "http://{}:{}/restconf/config/opendaylight-inventory:nodes/node/{}/flow-node-inventory:table/{}/flow/{}"\
            .format(self.address, self.port, switch, table, id)
        print link
        payload = {
                "flow": {
                    "priority": priority,
                    "flow-name": flow_name,
                    "id": id,
                    "table_id": table
                }
            }

        if ip:
            payload["flow"]["match"] = {
                        "ethernet-match": {
                            "ethernet-type": {
                                "type": "2048"
                            }
                        },
                        "ipv4-destination": ip
                    }

        if instruction:
            payload["flow"]["instructions"] = {
                "instruction": instruction
            }

        print(payload)
        print(json.dumps(payload))

        header={"Accept": "*/*",
            "Cache-Control": "no-cache",
            "Content-Type": "application/yang.data+json"}

        response = requests.put(link, json.dumps(payload), auth=(self.user, self.password),headers=header)
        return response

    def remove_flow(self,switch, table, id):
        link = "http://{}:{}/restconf/config/opendaylight-inventory:nodes/node/{}/flow-node-inventory:table/{}/flow/{}"\
            .format(self.address, self.port, switch, table, id)

        response = requests.delete(link)
        return response


