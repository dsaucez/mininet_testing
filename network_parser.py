import Switch
class Network_parser(object):
    def __init__(self, file_path):
        self.links=[]
        with open(file_path) as f:
            #TODO: check the network format in input
            f.readline()
            for line in f:
                self.links.append(tuple(line.split()))


    def create_network(self):
        network = dict()
        for switch in self.__get_switches():
            network[switch] = Switch.Switch(switch)
        #TODO: add the links

    def __get_switches(self):
        switches = []
        for s1, s2 in self.links:
            switches.append(s1)
            switches.append(s2)
        return set(switches)


class Request_parser(object):
    None