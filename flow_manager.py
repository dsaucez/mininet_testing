import ODL_client as Controller_client
from copy import deepcopy
import abc
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
    def __init__(self, network, solution, controller_address, port="8181", user="admin", password="admin"):
        self.controller_address = controller_address
        self.port = port
        self.user = user
        self.password = password
        self.solution = solution
        self.network = self.__create_extended_network(network)

    def __create_extended_network(self, network):
        extended_network = deepcopy(network)
        for switch in extended_network.keys():
            extended_network[switch].client = Controller_client.Client(address=self.controller_address, port=self.port,
                                                                       user=self.user, password=self.password)
            extended_network[switch].__class__ = ExtendedSwitch
        return extended_network

    @abc.abstractmethod
    def install_flows_to_controller(self):
        None


class SimpleFlowManager(FlowManager):
    def __init__(self, network, solution, controller_address, port="8181", user="admin", password="admin"):
        super(SimpleFlowManager, self).__init__(network, solution, controller_address, port=port,
                                                user=user, password=password)


    def install_flows_to_controller(self):






