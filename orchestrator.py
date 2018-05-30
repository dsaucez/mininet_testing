import network_parser, flow_manager, mininet_manager


class Orchestrator(object):

    def create_network_parser(self, network_file_path):
        return network_parser.NetworkParser(network_file_path)

    def create_request_parser(self, request_file_path):
        return network_parser.RequestParser(request_file_path)

    def create_flow_manager(self,network):
        return flow_manager.FlowManager(network)

    def create_network_builder(self, network, request):
        return mininet_manager.NetworkBuilder(network)

