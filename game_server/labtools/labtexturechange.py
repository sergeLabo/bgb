#!/usr/bin/python3
# -*- coding: UTF-8 -*-

## labTextureChange.py

#############################################################################
# Copyright (C) SergeBlender October 2016

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

"""
Class générique qui permet de changer la texture d'un objet
"""

from bge import logic as gl
from bge import texture

class TextureChange():
    ''' Classe générique utilisable dans d'autres projects,
        pour changer une texture image.'''

    def __init__(self, obj, old_tex):
        ''' obj     = objet concerné
            old_tex = texture originale
            new_tex = nouvelle texture '''
        self.obj = obj
        self.old_tex = old_tex
        # ID de la texture existante
        self.ID = texture.materialID(obj, 'IM' + old_tex)
        # Sauvegarde de l'objet python dans le Game Logic
        self.obj_texture = texture.Texture(obj, self.ID)

    def texture_new(self, new_tex):
        ''' Application de la nouvelle texture'''

        # Nouvelle source
        self.url = gl.expandPath(new_tex)
        print("Path du fichier", new_tex, "=", self.url)
        self.new_source = texture.ImageFFmpeg(self.url)

        # Remplacement
        self.obj_texture.source = self.new_source
        self.obj_texture.refresh(False)

    def texture2old(self):
        ''' Effacement de l'objet python, pour retourner à l'ancienne texture
            Cette fonction n'a jamais été utilisée !
        '''

        try:
            del self.obj_texture
        except:
            print("Problème avec la suppression de la texture:", self.obj_texture)
