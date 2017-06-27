#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

import sys
from time import sleep


class MulticastClient(DatagramProtocol):

    def startProtocol(self):
        # Join the multicast address, so we can receive replies:
        self.transport.joinGroup("228.0.0.5")
        # Send to 228.0.0.5:8005 - all listeners on the multicast address
        # (including us) will receive this message.
        self.transport.write(('Client: Ping').encode("utf-8"), ("228.0.0.5", 8005))

    def datagramReceived(self, datagram, address):
        print("Datagram %s received from %s" % (datagram, address))
        self.transport.write(('Client: Ping').encode("utf-8"), ("228.0.0.5", 8005))
        sleep(1)


class MulticastServer(DatagramProtocol):

    def startProtocol(self):
        """
        Called after protocol has started listening.
        """
        # Set the TTL>1 so multicast will cross router hops:
        self.transport.setTTL(5)
        # Join a specific multicast group:
        self.transport.joinGroup("228.0.0.5")

    def datagramReceived(self, datagram, address):
        print("Datagram %s received from %s" % (datagram, address))
        if datagram == "Client: Ping":
            # Rather than replying to the group multicast address, we send the
            # reply directly (unicast) to the originating port:
            self.transport.write(("Server: Pong").encode("utf-8"), address)


def run_client():
    reactor.listenMulticast(8005, MulticastClient(), listenMultiple=True)
    reactor.run()

def run_server():
    '''We use listenMultiple=True so that we can run MulticastServer.py and
    MulticastClient.py on same machine.
    '''

    reactor.listenMulticast(8005, MulticastServer(), listenMultiple=True)
    reactor.run()

def main(opt):

    if opt == "server":
        run_server()

    if opt == "client":
        run_client()


if __name__ == '__main__':
    '''Lancement du script avec:
    python3 labmulticasttwisted.py server
    ou
    python3 labmulticasttwisted.py client
    '''

    opt = sys.argv[1]
    main(opt)
