#! /usr/bin/python3
# -*- coding: UTF-8 -*-

#############################################################################
# Copyright (C) Labomedia June 2016
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franproplin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#############################################################################

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

'''
IRC bot avec twisted en python 3.x
'''


import time, sys

import twisted.words
from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
from twisted.python import log

from point_is_valid_old import point_is_valid

class IrcTwisted(irc.IRCClient):
    '''An IRC bot.'''

    #nickname = "twistedbot"

    def connectionMade(self):

        irc.IRCClient.connectionMade(self)
        print("Connection Made")

    def connectionLost(self, reason):

        irc.IRCClient.connectionLost(self, reason)
        print("Connection Lost {}".format(reason))

    # callbacks for events
    def signedOn(self):
        '''Called when bot has succesfully signed on to server.'''

        self.join(self.factory.channel)

    def joined(self, channel):
        '''This will get called when the bot joins the channel.'''

        print("Le bot a rejoint le channel {}".format(channel))

    def privmsg(self, user, channel, msg):
        '''Réception d'un message public ou privé.'''

        print(msg)

        # si le message est un cube, j'envoie à UDP
        is_valid, x, y, z , c = point_is_valid(msg)
        if is_valid:
            print("Point valide:", x, y, z , c)

        return msg

    def action(self, user, channel, msg):
        '''This will get called when the bot sees someone do an action.'''

        user = user.split('!', 1)[0]

    # irc callbacks
    def irc_NICK(self, prefix, params):
        '''Called when an IRC user changes their nickname.'''

        old_nick = prefix.split('!')[0]
        new_nick = params[0]


class IrcTwistedFactory(protocol.ClientFactory):
    '''A factory for IrcTwisteds.
    A new protocol instance will be created each time we connect to the server.
    '''

    def __init__(self, channel):
        self.channel = channel

    def buildProtocol(self, addr):
        p = IrcTwisted()
        p.factory = self
        return p

    def clientConnectionLost(self, connector, reason):
        '''If we get disconnected, reconnect to server.'''

        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print("connection failed:", reason)
        reactor.stop()


if __name__ == '__main__':

    server = 'jeuxlibres.org'
    channel = "#jeuxlibres"
    server = 'jeuxlibres.org'
    port = 6667

    # initialize logging
    log.startLogging(sys.stdout)

    # create factory protocol and application
    f = IrcTwistedFactory(channel)

    # connect factory to this host and port
    reactor.connectTCP(server, port, f)

    # run bot
    reactor.run()
