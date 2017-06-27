#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

## labformatter.py

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

"""
Sortie en terminal bien présentée !
"""

from collections import OrderedDict


class Formatter(object):
    def __init__(self):
        self.types = {}
        self.htchar = '\t'
        self.lfchar = '\n'
        self.indent = 0
        self.set_formater(object, self.__class__.format_object)
        self.set_formater(dict, self.__class__.format_dict)
        self.set_formater(list, self.__class__.format_list)
        self.set_formater(tuple, self.__class__.format_tuple)
        self.set_formater(OrderedDict, self.__class__.format_ordereddict)


    def set_formater(self, obj, callback):
        self.types[obj] = callback

    def __call__(self, value, **args):
        for key in args:
            setattr(self, key, args[key])
        formater = self.types[type(value) if type(value) in self.types else object]
        return formater(self, value, self.indent)

    def format_object(self, value, indent):
        return repr(value)

    def format_dict(self, value, indent):
        items = [
            self.lfchar + self.htchar * (indent + 1) + repr(key) + ': ' +
            (self.types[type(value[key]) if type(value[key]) in self.types else object])(self, value[key], indent + 1)
            for key in value
        ]
        return '{%s}' % (','.join(items) + self.lfchar + self.htchar * indent)

    def format_list(self, value, indent):
        items = [
            self.lfchar + self.htchar * (indent + 1) + (self.types[type(item) if type(item) in self.types else object])(self, item, indent + 1)
            for item in value
        ]
        return '[%s]' % (','.join(items) + self.lfchar + self.htchar * indent)

    def format_tuple(self, value, indent):
        items = [
            self.lfchar + self.htchar * (indent + 1) + (self.types[type(item) if type(item) in self.types else object])(self, item, indent + 1)
            for item in value
        ]
        return '(%s)' % (','.join(items) + self.lfchar + self.htchar * indent)

    def format_ordereddict(self, value, indent):
        items = [
            self.lfchar + self.htchar * (indent + 1) +
            "(" + repr(key) + ', ' + (self.types[
                type(value[key]) if type(value[key]) in self.types else object
            ])(self, value[key], indent + 1) + ")"
            for key in value
        ]
        return 'OrderedDict([%s])' % (','.join(items) +
               self.lfchar + self.htchar * indent)


if __name__ == '__main__':

    dict_a = {  1:"quooi",
                2: 1,
                3: 1.235,
                "gdfgs": ["ghgh", 1, 1.25, (1, 2)]}

    list_b =["ghgh", 1, 1.25, (1, 2)]

    for i in [dict_a, list_b]:

        print("Pretty:", type(i))
        pretty = Formatter()
        print(pretty(i))
