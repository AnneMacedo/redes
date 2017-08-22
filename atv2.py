#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import  Controller, OVSKernelAP
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def topology():
    net = Mininet(controller=Controller, link=TCLink, accessPoint=OVSKernelAP)

    print "*** Creating nodes"
    h1 = net.addStation('h1', ip='172.16.10.1/27')
    h2 = net.addStation('h2', ip='172.16.10.2/27')
    s1 = net.addSwitch('s1')
    c0 = net.addController('c0', controller=Controller, ip='172.16.10.0', port=6633)

    net.configureWifiNodes()

    net.addLink(h1, s1)
    net.addLink(h2, s1)

    net.build()
    c0.start()
    s1.start([c0])
 
    CLI(net)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
topology()
