#!/usr/bin/env python
# -*- coding: utf-8 -*-

__copyright__ = """
   pySART - Simplified AUTOSAR-Toolkit for Python.

   (C) 2010-2018 by Christoph Schueler <cpu12.gems.googlemail.com>

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


from pydbc.api.base import BaseObject


class EnvVar(BaseObject):
    """
    """
    # {'Type': 0, 'Unit': '', 'Comment': 'Enable the ECU', 'Size': None, 'Name': 'EnvTPMS_ILEnable',
    # 'Startup_Value': 1.0, 'RID': 72, 'Access': 0, 'Maximum': 1.0, 'Minimum': 0.0}

    OBJECT_TYPE = AttributeType.ENV_VAR
    TABLE_NAME = "EnvVar"

    KEY = 'rid'
    COLUMNS = (
        ('name', 'Name'),
        ('_type', 'Type'),
        ('access', 'Access'),
        ('size', 'Size'),
        ('initialValue', 'Startup_Value'),
        ('min', 'Minimum'),
        ('max', 'Maximum'),
        ('comment', 'Comment'),
    )

    def __init__(self, database, rid, name, _type, access, size, initialValue, min, max, comment):
        super(EnvVar, self).__init__(database)
        self.rid = rid
        self.name = name
        self._type = _type
        self.access = access
        self.size = size
        self.initialValue = initialValue
        self.min = min
        self.max = max
        self.comment = comment

