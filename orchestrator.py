import network_parser, flow_manager, mininet_manager, solution_parser


class Orchestrator(object):
    def __init__(self, network_file_path, request_file_path, solution_file_path):
        self.network_parser = self.__create_network_parser(network_file_path)
        self.request_parser = self.__create_request_parser(request_file_path)

        network_parsed = self.network_parser.create_network()
        request_parsed = self.request_parser.create_request()

        self.network_builder = self.__create_network_builder(network=network_parsed, request=request_parsed)
        self.solution_parser = self.__create_solution_parser(solution_file_path)

        solution_parsed = self.solution_parser.create_solution()
        self.flow_manager = self.__create_flow_manager(network=network_parsed, solution=solution_parsed)

        self.network_tester = self.__create_network_tester()

    def __create_network_parser(self, network_file_path):
        return network_parser.NetworkParser(network_file_path)

    def __create_request_parser(self, request_file_path):
        return network_parser.RequestParser(request_file_path)

    def __create_flow_manager(self, network, solution):
        return flow_manager.SimpleFlowManager(network, solution)

    def __create_network_builder(self, network, request):
        return mininet_manager.NetworkBuilder(network, request)

    def __create_solution_parser(self, solution_file_path):
        return solution_parser.Solution_parser(solution_file_path)

    def __create_network_tester(self, **kwargs):
        None

