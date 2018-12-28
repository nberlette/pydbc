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

from collections import namedtuple

import antlr4

class LdfListener(antlr4.ParseTreeListener):


    def exitLin_description_file(self, ctx):
        self.value = dict(
            protocolVersion = ctx.pv.value,
            languageVersion = ctx.lv.value,
            speed = ctx.ls.value,
            channelName = ctx.cn.value if ctx.cn else None,
            nodes = ctx.ndef.value,
            nodeCompositions = ctx.ncdef.value if ctx.ncdef else None,
            signals = ctx.sdef.value,
            diagnosticSignals = ctx.dsdef.value if ctx.dsdef else None,
            frames = ctx.fdef.value,
            sporadicFrames = ctx.sfdef.value if ctx.sfdef else None,
            eventTriggeredFrames = ctx.etfdef.value if ctx.etfdef else None,
            diagnosticFrames = ctx.dffdef.value if ctx.dffdef else None,
            nodeAttributes = ctx.nadef.value,
            scheduleTables = ctx.stdef.value,
            signalGroups = ctx.sgdef.value if ctx.sgdef else None,
            signalEncodings = ctx.setdef.value if ctx.setdef else None,
            signalRepresentations = ctx.srdef.value if ctx.srdef else None,
        )

    def exitLin_protocol_version_def(self, ctx):
        ctx.value = ctx.s.value

    def exitLin_language_version_def(self, ctx):
        ctx.value = ctx.s.value

    def exitLin_speed_def(self, ctx):
        ctx.value = ctx.n.value

    def exitChannel_name_def(self, ctx):
        ctx.value = ctx.i.value

    def exitNode_def(self, ctx):
        mname = ctx.mname.value
        tb = ctx.tb.value
        j = ctx.j.value
        snames = [x.value for x in ctx.snames]
        ctx.value = dict(master = mname, timeBase = tb, jitter = j, slaves = snames)

    def exitNode_name(self, ctx):
        ctx.value = ctx.i.value

    def exitTime_base(self, ctx):
        ctx.value = ctx.n.value

    def exitJitter(self, ctx):
        ctx.value = ctx.n.value

    def exitNode_attributes_def(self, ctx):
        items = [x.value for x in ctx.items]
        ctx.value = items

    def exitNode_attribute(self, ctx):
        name = ctx.name.value
        version = ctx.version.value
        n0 = ctx.n0.value
        n1 = ctx.n1.value
        attrs = ctx.attrs.value
        ctx.value = dict(name = name, version = version, configuredNAD = n0, initialNAD = n1, attrs = attrs)

    def exitProtocol_version(self, ctx):
        ctx.value = ctx.s.value

    def exitDiag_address(self, ctx):
        ctx.value = ctx.i.value

    def exitAttributes_def(self, ctx):
        sid = ctx.sid.value
        fid = ctx.fid.value
        v = ctx.v.value if ctx.v else None
        sn0 = ctx.sn0.value
        sn1s = [x.value for x in ctx.sn1s]
        cf = ctx.cf.value
        p2Min = ctx.p2Min.value
        stMin = ctx.stMin.value
        nAs = ctx.nAs.value
        nCr = ctx.nCr.value
        ctx.value = dict(supplierID = sid, functionID = fid, variant = v, responseErrorSignal = sn0, faultStateSignals = sn1s,
                p2Min = p2Min, stMin = stMin, nAs = nAs, nCr = nCr, configurableFrames = cf
        )

    def exitSupplier_id(self, ctx):
        ctx.value = ctx.i.value

    def exitFunction_id(self, ctx):
        ctx.value = ctx.i.value

    def exitVariant(self, ctx):
        ctx.value = ctx.i.value

    def exitSignal_name(self, ctx):
        ctx.value = ctx.i.value

    def exitConfigurable_frames(self, ctx):
        ctx.value = [x.value for x in ctx.frames]

    def exitConfigurable_frame(self, ctx):
        fname = ctx.fname.value
        mid = ctx.mid.value if ctx.mid else None
        ctx.value = dict(frameName = fname, messageID = mid)

    def exitMessage_id(self, ctx):
        ctx.value = ctx.i.value

    def exitNode_composition_def(self, ctx):
        ctx.value = [x.value for x in ctx.items]

    def exitConfiguration(self, ctx):
        cname = ctx.cname.value
        items = [x.value for x in ctx.items]
        ctx.value = dict(configurationName = cname, items = items)

    def exitConfiguration_item(self, ctx):
        cnode = ctx.cnode.value
        lnodes = [x.value for x in ctx.lnodes]
        ctx.value = dict(compositeNode = cnode, logicalNodes = lnodes)

    def exitConfiguration_name(self, ctx):
        ctx.value = ctx.i.value

    def exitComposite_node(self, ctx):
        ctx.value = ctx.i.value

    def exitLogical_node(self, ctx):
        ctx.value = ctx.i.value

    def exitSignal_def(self, ctx):
        ctx.value = [x.value for x in ctx.items]

    def exitSignal_item(self, ctx):
        sname = ctx.sname.value
        ssize = ctx.ssize.value
        initValue = ctx.initValue.value
        pub = ctx.pub.value
        sub = [x.value for x in ctx.sub]
        ctx.value = dict(name = sname, size = ssize, initValue = initValue, publishedBy = pub, subscribedBy = sub)

    def exitSignal_size(self, ctx):
        ctx.value = ctx.i.value

    def exitInit_value(self, ctx):
        scalar = ctx.s.value if ctx.s else None
        array = ctx.a.value if ctx.a else None
        ctx.value = dict(scalar = scalar, array = array)

    def exitInit_value_scalar(self, ctx):
        ctx.value = ctx.i.value

    def exitInit_value_array(self, ctx):
        ctx.value = [x.value for x in ctx.vs]

    def exitPublished_by(self, ctx):
        ctx.value =  ctx.i.value

    def exitSubscribed_by(self, ctx):
        ctx.value =  ctx.i.value

    def exitDiagnostic_signal_def(self, ctx):
        ctx.value = [x.value for x in ctx.items]

    def exitDiagnostic_item(self, ctx):
        name = ctx.name.value
        size = ctx.size.value
        initValue = ctx.initValue.value
        ctx.value = dict(name = name, size = size, initValue = initValue)

    def exitSignal_groups_def(self, ctx):
        ctx.value = [x.value for x in ctx.items]

    def exitSignal_group(self, ctx):
        sgname = ctx.sgname.value
        gsize = ctx.gsize.value
        items = [x.value for x in ctx.items]
        ctx.value = dict(signalGroupName = sgname, groupSize = gsize, items = items)

    def exitSignal_group_item(self, ctx):
        sname = ctx.sname.value
        goffs = ctx.goffs.value
        ctx.value = dict(signalName = sname, groupOffset = goffs)

    def exitSignal_group_name(self, ctx):
        ctx.value = ctx.i.value

    def exitGroup_size(self, ctx):
        ctx.value = ctx.i.value

    def exitGroup_offset(self, ctx):
        ctx.value = ctx.i.value

    def exitFrame_def(self, ctx):
        ctx.value = [x.value for x in ctx.items]

    def exitFrame_item(self, ctx):
        fname = ctx.fname.value
        fid = ctx.fid.value
        p = ctx.p.value
        fsize = ctx.fsize.value
        items = [x.value for x in ctx.items]
        ctx.value = dict(frameName = fname, frameID = fid, publishedBy = p, frameSize = fsize, signals = items)

    def exitFrame_signal(self, ctx):
        sname = ctx.sname.value
        soffs = ctx.soffs.value
        ctx.value = dict(signalName = sname, signalOffset = soffs)

    def exitFrame_name(self, ctx):
        ctx.value = ctx.i.value

    def exitFrame_id(self, ctx):
        ctx.value = ctx.i.value

    def exitFrame_size(self, ctx):
        ctx.value = ctx.i.value

    def exitSignal_offset(self, ctx):
        ctx.value = ctx.i.value

    def exitSporadic_frame_def(self, ctx):
        ctx.value = [x.value for x in ctx.items]

    def exitSporadic_frame_item(self, ctx):
        name = ctx.sfn.value
        fnames = [x.value for x in ctx.names]
        ctx.value = dict(sporadicFrameName = name, frameNames = fnames)

    def exitSporadic_frame_name(self, ctx):
        ctx.value = ctx.i.value

    def exitEvent_triggered_frame_def(self, ctx):
        ctx.value = [x.value for x in ctx.items]

    def exitEvent_triggered_frame_item(self, ctx):
        e = ctx.e.value
        c = ctx.c.value
        fid = ctx.fid.value
        items = [x.value for x in ctx.items]
        ctx.value = dict(frameName = e, frameID = fid, scheduleTable = c, frameNames = items)

    def exitEvent_trig_frm_name(self, ctx):
        ctx.value = ctx.i.value

    def exitCollision_resolving_schedule_table(self, ctx):
        ctx.value = ctx.i.value

    def exitDiag_frame_def(self, ctx):
        mid = ctx.mid.value
        sid = ctx.sid.value
        mitems = [x.value for x in ctx.mitems]
        sitems = [x.value for x in ctx.sitems]
        ctx.value = dict(masterID = mid, slaveID = sid, masterSignals = mitems, slaveSignals = sitems)

    def exitDiag_frame_item(self, ctx):
        sname = ctx.sname.value
        soffs = ctx.soffs.value
        ctx.value = dict(signalName = sname, signalOffset = soffs)

    def exitSchedule_table_def(self, ctx):
        ctx.value = [x.value for x in ctx.items]

    def exitSchedule_table_entry(self, ctx):
        s = ctx.s.value
        items = [x.value for x in ctx.items]
        ctx.value = dict(name = s, commands = items)

    def exitSchedule_table_command(self, ctx):
        c = ctx.c.value
        f = ctx.f.value
        ctx.value = dict(command = c, frameTime = f)

    def exitSchedule_table_name(self, ctx):
        ctx.value = ctx.i.value

    def exitCommand(self, ctx):
        if ctx.frameName:
            cmd = ctx.frameName.value
        else:
            cmd = ctx.c.value
        if cmd == 'AssignNAD':
            nodeName = ctx.nodeName.value
        elif cmd == 'ConditionalChangeNAD':
            nad = ctx.nad.value
            id_ = ctx.id_.value
            byte_ = ctx.byte_.value
            mask = ctx.mask.value
            inv = ctx.inv.value
            newNad = ctx.new_NAD.value
        elif cmd == 'DataDump':
            nodeName = ctx.nodeName.value
            d1 = ctx.d1.value
            d2 = ctx.d2.value
            d3 = ctx.d3.value
            d4 = ctx.d4.value
            d5 = ctx.d5.value
        elif cmd == 'SaveConfiguration':
            nodeName = ctx.nodeName.value
        elif cmd == 'AssignFrameIdRange':
            nodeName = ctx.nodeName.value
            frameIndex = ctx.frameIndex.value
            pids = [p.value for p in ctx.p]
        elif cmd == 'FreeFormat':
            d1 = ctx.d1.value
            d2 = ctx.d2.value
            d3 = ctx.d3.value
            d4 = ctx.d4.value
            d5 = ctx.d5.value
            d6 = ctx.d6.value
            d7 = ctx.d7.value
            d8 = ctx.d8.value
        elif cmd == 'AssignFrameId':
            nodeName = ctx.nodeName.value
            frameName = ctx.frameName.value
        else:
            d1 = d2 = d3 = d4 = d5 = d6 = d7 = d8 = None
        ctx.value = dict(command = cmd)

    def exitFrame_index(self, ctx):
        ctx.value = ctx.i.value

    def exitFrame_PID(self, ctx):
        ctx.value = ctx.i.value

    def exitFrame_time(self, ctx):
        ctx.value = ctx.n.value

    def exitSignal_encoding_type_def(self, ctx):
        items = [x.value for x in ctx.items]
        ctx.value = items

    def exitSignal_encoding_entry(self, ctx):
        s = ctx.s.value
        items = [x.value for x in ctx.items]
        ctx.value = dict(name = s, values = items)

    def exitSignal_encoding_value(self, ctx):
        if ctx.l:
            value = ctx.l.value
            vtype = "logical"
        elif ctx.p:
            value = ctx.p.value
            vtype = "range"
        elif ctx.b:
            value = ctx.b.value
            vtype = "bcd"
        elif ctx.a:
            value = ctx.a.name
            vtype = "ascii"
        ctx.value = dict(value = value, valueType = vtype)


    def exitSignal_encoding_type_name(self, ctx):
        ctx.value = ctx.i.value

    def exitLogical_value(self, ctx):
        pass

    def exitPhysical_range(self, ctx):
        minValue = ctx.minValue.value
        maxValue = ctx.maxValue.value
        scale = ctx.scale
        offset = ctx.offset
        ctx.value = dict(min = minValue, max = maxValue, scale = scale, offset = offset)

    def exitBcd_value(self, ctx):
        pass

    def exitAscii_value(self, ctx):
        pass

    def exitSignal_value(self, ctx):
        ctx.value = ctx.i.value

    def exitMin_value(self, ctx):
        ctx.value = ctx.i.value

    def exitMax_value(self, ctx):
        ctx.value = ctx.i.value

    def exitScale(self, ctx):
        ctx.value = ctx.n.value

    def exitOffset(self, ctx):
        ctx.value = ctx.n.value

    def exitText_info(self, ctx):
        ctx.value = ctx.s.value

    def exitSignal_representation_def(self, ctx):
        items = [x.value for x in ctx.items]
        ctx.value = items

    def exitSignal_representation_entry(self, ctx):
        enc = ctx.enc.value
        names = [x.value for x in ctx.names]
        ctx.value = dict(name = enc, signalNames = names)

    def exitIntValue(self, ctx):
        if ctx.i:
            ctx.value = int(ctx.i.text, 10)
        elif ctx.h:
            ctx.value = int(ctx.h.text, 16)

    def exitFloatValue(self, ctx):
        ctx.value = float(ctx.f.text) if ctx.f else None

    def exitNumber(self, ctx):
        ctx.value = ctx.i.value if ctx.i else ctx.f.value

    def exitStringValue(self, ctx):
        ctx.value = ctx.s.text.strip('"') if ctx.s else None

    def exitIdentifierValue(self, ctx):
        ctx.value = ctx.i.text if ctx.i else None

