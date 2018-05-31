from mininet.topo import Topo
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections


class SimpleTopology(Topo):
    # Single switch connected to n hosts
    def build(self):
        # Initialize topology and default
        switches = []
        hosts = []

        # create switches
        for s in range(6):
            switches.append(self.addSwitch('s%s' % (s + 1), protocols='OpenFlow13'))

        # create hosts
        for h in range(8):
            hosts.append(self.addHost('h%s' % (h + 1)))

        self.addLink(hosts[0], switches[0])
        self.addLink(hosts[1], switches[0])
        self.addLink(hosts[2], switches[1])
        self.addLink(hosts[3], switches[1])
        self.addLink(hosts[4], switches[4])
        self.addLink(hosts[5], switches[4])
        self.addLink(hosts[6], switches[5])
        self.addLink(hosts[7], switches[5])

        self.addLink(switches[0], switches[2])
        self.addLink(switches[1], switches[2])
        self.addLink(switches[2], switches[3])
        self.addLink(switches[3], switches[4])
        self.addLink(switches[3], switches[5])



