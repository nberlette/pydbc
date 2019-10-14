#!/usr/bin/env python
# -*- coding: utf-8 -*-

__copyright__ = """
   pySART - Simplified AUTOSAR-Toolkit for Python.

   (C) 2010-2019 by Christoph Schueler <cpu12.gems.googlemail.com>

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


from pydbc.logger import Logger

class BaseLoader(object):

    def __init__(self, db, queryClass):
        self.db = db
        self.queries = queryClass(db)
        self.logger = Logger(__name__)

    def insertValues(self, tree):
        cur = self.db.getCursor()
        self.db.beginTransaction()
        self._insertValues(cur, tree)
        self.db.commitTransaction()
