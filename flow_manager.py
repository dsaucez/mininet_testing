import ODL_client as Controller_client

import Switch


class ExtendedSwitch(Switch.Switch):
    def __init__(self, id, address, port="8181", user="admin", password="admin"):
        super(ExtendedSwitch, self).__init__(id)
        self.client = Controller_client.Client(address, port=port, user=user, password=password)

    def add_flow(self, table_id, flow):
        super(ExtendedSwitch, self).add_flow(table_id, flow)
        self.client.add_flow(switch=self.id, table=table_id, id=flow.id,
                             priority=flow.priority, flow_name=flow.name,
                             ipv4=flow.ipv4, instruction=flow.instruction)
        # TODO: add exceptions

    def remove_flow(self,table_id, flow_id):
        super(ExtendedSwitch, self).remove_flow(table_id, flow_id)
        self.client.remove_flow(switch=self.id, table=table_id, id=flow_id)
        # TODO: add exceptions

    def get_flows(self):
        return self.client.get_flows(switch=self.id)


class FlowManager(object):
    def __init__(self, network):
        self.network = network







