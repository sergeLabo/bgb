#!/usr/bin/python
# -*- coding: UTF-8 -*-

## labtcpclient.py

#############################################################################
# Copyright (C) Labomedia  October 2016
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

import socket
from time import sleep


class LabTcpClient(object):
    '''Envoi et réception sur le même socket en TCP.
    Toutes les méthodes sont sans try.
    '''

    def __init__(self, ip, port):

        self.ip = ip
        self.port = port
        self.server_address = (ip, port)
        self.data = None
        self.sock = None
        self.create_socket()

    def create_socket(self):
        '''Création du socket sans try, et connexion.'''

        while not self.sock:

            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(self.server_address)

            print("Création du socket client {}".format(self.server_address))

            sleep(0.1)

    def send(self, msg):
        '''Envoi d'un message, avec send.'''

        self.sock.send(msg)

    def reconnect(self):
        '''Reconnexion.'''

        self.sock = None
        self.create_socket()

    def close(self):
        '''Close the socket.'''

        self.sock.close()
        self.sock = None

    def listen(self):
        '''Return received data.'''

        raw_data = None

        raw_data = self.sock.recv()

        return raw_data


if __name__ == "__main__":

    ip = "127.0.0.1"
    port = 8000

    titre_liste = [   "1_05_Tu_commences_a_me_plaire.ogg",
                        "16_Ironside_Excerpt.ogg",
                        "636_Suite_fur_Violoncello_solo_No.ogg",
                        "18_Yakuza_Oren_1.ogg",
                        "2_01_Intro_Versailles.ogg"]

    clt = LabTcpClient(ip, port)

    for titre in titre_liste:
        titre = titre.encode("utf-8")
        sleep(0.5)
        clt.send(titre)

    clt.close()
