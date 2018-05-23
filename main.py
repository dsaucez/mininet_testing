from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController, Controller
from Topologies import SimpleTopology
from mininet.log import setLogLevel
from mininet.cli import CLI
from os import system


def change_ip(network):
    network["h1"].setIP(ip="10.0.1.1", prefixLen=24)
    network["h2"].setIP(ip="10.0.1.2", prefixLen=24)


setLogLevel('info')
system("sudo mn -c")

remote_controller = RemoteController('c0', ip='127.0.0.1', port=6633)
# lc0 = Controller ("c1",protocols="OpenFlow13")
net = Mininet(topo=SimpleTopology(), switch=OVSSwitch, build=False)
net.addController(remote_controller)

net.build()

change_ip(network=net)

net.start()
CLI(net)
net.stop()
