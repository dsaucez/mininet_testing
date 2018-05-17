from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController, Controller
from Topologies import SimpleTopology
from mininet.log import setLogLevel
from mininet.cli import CLI

setLogLevel( 'info' )


rc0 = RemoteController( 'c0', ip='192.168.56.102', port=6633 )
lc0 = Controller ("c1",protocols="OpenFlow13")
topo = SimpleTopology()
net = Mininet(topo=topo, switch=OVSSwitch, build=False)
net.addController(rc0)
net.build()
net.start()
CLI(net)
net.stop()

