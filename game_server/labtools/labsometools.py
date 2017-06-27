#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

## labsometools.py

#############################################################################
# Copyright (C) Labomedia November 2013
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

import inspect
import subprocess,re, socket
from functools import reduce
try:
    from bge import logic as gl
except:
    pass

class VirtualGl():
    ''' Classe vide pour simuler
    from bge import logic as gl
    Dommage que ça ne serve pas à grand chose
    '''
    def __init__(self):
        pass

def scene_change(sceneOld, sceneNew):
    '''
    End of sceneOld, load sceneNew.
    Scene must be str: if scene = scene python object, name is scene.name
    '''
    scenes = gl.getSceneList()
    print("Scenes list in scene_change() =", scenes)
    # Check name
    scnName = []
    for scn in scenes:
        scnName.append(scn.name)
    if not sceneOld in scnName:
        print("  {} isn't in scenes list".format(sceneOld))
    else:
        gl.tempoDict["scene_change"].unlock()
        gl.tempoDict["scene_change"].reset()
        print("  Tempo scene_change reset and unlock")

        for scn in scenes:
            if scn.name == sceneOld:
                scn.end()
                print("  End of scene: {}".format(scn))
        try:
            gl.addScene(sceneNew)
            print("  Scene {0} added".format(sceneNew))
        except:
            print("  Scene {0} doesn't exist: Can't be set.".format(sceneNew))

def get_my_ip():
    '''
        Get local ip
        A generator that returns stripped lines of output from "ip address show"
    '''

    iplines=(line.strip() for line in \
                        subprocess.getoutput("ip address show").split('\n'))

    #Turn that into a list of IPv4 and IPv6 address/mask strings
    addresses1=reduce(lambda a,v:a+v,(re.findall(r"inet ([\d.]+/\d+)",line) \
            +re.findall(r"inet6 ([\:\da-f]+/\d+)",line) for line in iplines))

    #Get a list of IPv4 addresses as (IPstring,subnetsize) tuples
    ipv4s=[(ip,int(subnet)) for ip,subnet in (addr.split('/') for addr in \
                                                addresses1 if '.' in addr)]

    my_ip = ipv4s[1][0]
    return my_ip

def print_str_args(*args):
    ''' Imprime en terminal les variables en argument
        Les variables doivent être sous forme de string,
        par exemple
        print_str_args("a")
        imprime la variable a qui a une valeur 42
        a = 42
        '''
    for i in args:
        record=inspect.getouterframes(inspect.currentframe())[1]
        frame=record[0]
        val=eval(i,frame.f_globals,frame.f_locals)
        print('{0} = {1}'.format(i, val))

def droiteAffine(x1, y1, x2, y2):
    ''' Retourne les valeurs de a et b de y=ax+b
        à partir des coordonnées de 2 points'''
    a = (y2 - y1) / (x2 - x1)
    b = y1 - (a * x1)
    return a, b

if __name__ == '__main__':
    # Only to test
    spam = 42
    a = 42
    c = [0,0]
    d = {"g":1, "1":2}

    ip =get_my_ip()

    print_str_args("a", "spam", "c", "d", "ip")
    ##print(droiteAffine(0, -30, 0.7, -20))
