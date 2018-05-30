import Switch


class NetworkParser(object):
    def __init__(self, file_path):
        parsed_file = self.__parse_file(file_path)
        self.links = self.__get_links(parsed_file)
        self.switches = self.__get_switches(parsed_file)

    def create_network(self):
        network = dict()
        for switch in self.switches:
            network[switch] = Switch.Switch(switch)
        for s1, s2 in self.links:
            network[s1].add_link(s1, s2)
            network[s2].add_link(s1, s2)
        return network

    def __get_switches(self, parsed_file):
        switches = []
        for s1, s2 in [tuple(x) for x in parsed_file]:
            switches.append(s1)
            switches.append(s2)
        return set(switches)

    def __get_links(self, parsed_file):
        return set([tuple(x) for x in parsed_file])

    def __parse_file(self, file_path):
        lines = []
        with open(file_path) as f:
            for line in f:
                lines.append(line.split())
        return lines


class RequestParser(object):
    def __init__(self, file_path):
        self.parsed_file = self.__parse_file(file_path)
        self.request = self.__create_request()

    def __create_request(self):
        requests = dict()
        for s1, s2, bw in self.parsed_file:
            requests[(s1, s2)] = float(bw)
        return requests

    def __parse_file(self, file_path):
        lines = []
        with open(file_path) as f:
            for line in f:
                lines.append(line.split())
        return lines
