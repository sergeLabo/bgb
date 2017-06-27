#!/usr/bin/python3
# -*- coding: UTF-8 -*-

## labudpclient.py

#############################################################################
# Copyright (C) Labomedia October 2016
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

'''

Recréer un socket avant chaque envoi ou réception, résoud les problèmes
de réseau, ça se reconnecte tout seul.
Par contre, le port éphémère du recvfrom changera à chaque fois.

Dans Blender, où il est impossible de créer un thread, socketserver,
ou d'utiliser asyncio, c'est très adapté.

Doit encore être testé, en particulier si défaut réseau, serveur etc ...

'''

import socket



class LabUdpClient():
    '''Envoi et reception en UDP.
    Cette classe n'encode pas le message à envoyer, sans try: .
    '''

    def __init__(self, buffer_size=1024, timeout=0.01):
        '''Création d'un socket UDP.
        buffer_size = entier, permet de vider le buffer à chaque lecture,
        pour avoir toujours la dernière valeur.
        '''

        self.buffer_size = buffer_size
        self.timeout = timeout

        # Socket UDP
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Le try de réception dure maxi le timeout
        self.sock.settimeout(self.timeout)

        # test car error avec asyncio
        self.sock.setblocking(False)

        # This option set buffer size
        # Every self.sock.recv() empty the buffer,
        # so we have always the last incomming value
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.buffer_size)

    def bind(self, addr):
        '''Quelle est la différence avec connect ?'''

        self.sock.bind(addr)

    def connect(self, addr):
        '''Connexion à l'adresse pour recevoir addr = tuple.'''

        self.sock.connect(addr)

    def send_to(self, req, address):
        '''Envoi à l'adresse = (ip, port).'''

        self.sock.sendto(req, address)

    def listen(self):
        '''Retourne les datas et l'adresse reçue.'''

        raw_data, addr = self.sock.recvfrom(self.buffer_size)

        return raw_data, addr

    def close(self):
        self.sock.close()
        self.sock = None



if __name__ == "__main__":

    # Test de cette classe
    from time import sleep
    import json

    ### test = 1 pour recevoir
    ### test = 0 pour envoyer
    ##test = 1

    ##if test == 0:
        ### Test de réception
        ##clt_receive = LabUdpClient()
        ##clt_receive.bind(("192.168.0.102", 8000))
        ##while 1:
            ##data, addr = clt_receive.listen()
            ##if data:
                ##print(data, addr)
            ##sleep(0.01)

    ##if test == 1:
        ### Test d'envoi
        ##clt_send = LabUdpClient()

        ##msg = {"quit": 1}
        ##msg = "quit"
        ##data = json.dumps(msg).encode("utf-8")

        ##clt_send.send_to(data, ("192.168.0.102", 8000))
        ##clt_send.close()


    # Test d'envoi
    for nb in range(10000):
        clt_send = LabUdpClient()

        data = {"phone": nb}
        data = json.dumps(data).encode("utf-8")

        clt_send.send_to(data, ("127.0.0.1", 9999))

        print("Envoi de {}".format(data))

        clt_send.close()

        # 60 Hz
        sleep(0.1)
