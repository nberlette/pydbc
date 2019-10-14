#!/usr/bin/env python
# -*- coding: utf-8 -*-

__copyright__ = """
   pySART - Simplified AUTOSAR-Toolkit for Python.

    ( C) 2010-2019 by Christoph Schueler <cpu12.gems.googlemail.com>

   All Rights Reserved

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License along
   with this program; if not, write to the Free Software Foundation, Inc.,
   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

   s. FLOSS-EXCEPTION.txt
"""
__author__  = 'Christoph Schueler'
__version__ = '0.1.0'

import colorama


class NullHilighter:

    def coloredText(self, color, msg):
        return msg

    def errorText(self, msg):
        return msg

    def successText(self, msg):
        return msg

    def progressText(self, msg):
        return msg


class ColorHilighter:

    def __init__(self):
        colorama.init(convert = args.winout, strip = False)

    def coloredText(self, color, msg):
        return "{}{}".format(color, msg)

    def errorText(self, msg):
        return coloredText(colorama.Fore.RED, msg)

    def successText(self, msg):
        return coloredText(colorama.Fore.GREEN, msg)

    def progressText(self, msg):
        return coloredText(colorama.Fore.BLUE, msg)

    def _resetColorStyle(self):
        print(colorama.Style.RESET_ALL, end = "", flush = True)


def makeHilighter(param):
    return NullHilighter()
