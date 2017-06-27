#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

## lab_getmyip.py

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

import os, sys
import subprocess, re
from functools import reduce


def get_my_ip():
    '''Retourne l'adresse ip du pc sur le réseau local.
    Valable pour python3.x
    '''

    #A generator that returns stripped lines of output from "ip address show"
    iplines = (line.strip() for line in subprocess.getoutput("ip address show")\
                                                           .split('\n'))
    #Turn that into a list of IPv4 and IPv6 address/mask strings
    addresses1=reduce(lambda a,v:a+v,(re.findall(r"inet ([\d.]+/\d+)",
                                    line)+re.findall(r"inet6 ([\:\da-f]+/\d+)",
                                    line) for line in iplines))
    #Get a list of IPv4 addresses as (IPstring,subnetsize) tuples
    ipv4s = [(ip,int(subnet)) for ip,subnet in (addr.split('/') for addr in\
                                              addresses1 if '.' in addr)]
    # my IP
    try:
        ip = ipv4s[1][0]
        print("IP =", ip)
    except:
        print("Cet ordinateur n'est pas connecté à un réseau !")
        ip = "127.0.0.1"

    return ip

if __name__ == '__main__':
    get_my_ip()
