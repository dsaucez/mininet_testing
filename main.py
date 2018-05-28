from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController, Controller
from Topologies import SimpleTopology
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections

from os import system


def change_ip(network):
    network["h1"].setIP(ip="10.0.1.1", prefixLen=24)
    network["h2"].setIP(ip="10.0.1.2", prefixLen=24)

def main():
    setLogLevel('info')
    system("sudo mn -c")

    remote_controller = RemoteController('c0', ip='127.0.0.1', port=6633, protocols="OpenFlow13")
    # lc0 = Controller ("c1",protocols="OpenFlow13")
    net = Mininet(topo=SimpleTopology(), switch=OVSSwitch, build=False)
    net.addController(remote_controller)

    net.build()

    change_ip(network=net)
    h1, h2, h3 = net.getNodeByName("h1", "h2", "h3")
    #net.iperf( ( h1, h2 ), l4Type='UDP' )

    net.start()
    CLI(net)
    net.stop()


if __name__=="__main__":
    main()