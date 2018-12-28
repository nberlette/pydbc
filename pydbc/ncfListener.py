# Generated from ncf.g4 by ANTLR 4.7

import antlr4

class NcfListener(antlr4.ParseTreeListener):

    def exitToplevel(self, ctx):
        v = ctx.v.value
        nodes = [x.value for x in ctx.nodes]
        self.value = dict(version = v, nodes = nodes)

    def exitLanguage_version(self, ctx):
        s = ctx.s.value
        ctx.value = s

    def exitNode_definition(self, ctx):
        name = ctx.name.value
        g = ctx.g.value
        d = ctx.d.value
        f = ctx.f.value
        e = ctx.e.value
        s = ctx.s.value
        t = ctx.t.value if ctx.t else None
        ctx.value = dict(name = name, general = g, diagnostic = d, frames= f, encodings = e, status = s, freeText = t)

    def exitNode_name(self, ctx):
        ctx.value = ctx.i.value

    def exitGeneral_definition(self, ctx):
        pv = ctx.pv.value
        sup = ctx.sup.value
        fun = ctx.fun.value
        var = ctx.var.value
        br = ctx.br.value
        tf = True if ctx.tf.text == "yes" else False
        ctx.value = dict(protocolVersion = pv, supplier = sup, function = fun, variant = var, bitrate = br, wakeupSignal = tf)

    def exitProtocol_version(self, ctx):
        ctx.value = ctx.s.value

    def exitSupplier_id(self, ctx):
        ctx.value = ctx.i.value

    def exitFunction_id(self, ctx):
        ctx.value = ctx.i.value

    def exitVariant_id(self, ctx):
        ctx.value = ctx.i.value

    def exitBitrate_definition(self, ctx):
        rates = br = minBr = maxBr = None
        if ctx.rates:
            rates = [x.value for x in ctx.rates]
        elif ctx.br:
            br = ctx.br.value
        else:
            minBr = ctx.minBr.value
            maxBr = ctx.maxBr.value
        ctx.value = dict(bitrate = br, minBr = minBr, maxBr = maxBr, rates = rates)

    def exitBitrate(self, ctx):
        ctx.value = ctx.n.value

    def exitDiagnostic_definition(self, ctx):
        lhs = ctx.lhs.value
        rhs = ctx.rhs.value if ctx.rhs else None
        nads = [x.value for x in ctx.nads] if ctx.nads else []
        dc = ctx.dc.value if ctx.dc else None
        p2Min = ctx.p2Min.value if ctx.p2Min else None
        stMin = ctx.stMin.value if ctx.p2Min else None
        nAs = ctx.nAs.value if ctx.nAs else None
        nCr = ctx.nCr.value if ctx.nCr else None
        sids = [x.value for x in ctx.sids] if ctx.sids else []
        mml = ctx.mml.value if ctx.mml else None
        ctx.value = dict(
            maxMessageLength = mml, lhs = lhs, rhs = rhs, nads = nads, diagnosticClass = dc, p2Min = p2Min, stMin = stMin, nAs = nAs, nCr = nCr, supportedSids = sids
        )

    def exitFrame_definition(self, ctx):
        frames = [x.value for x in ctx.frames]
        ctx.value = frames

    def exitSingle_frame(self, ctx):
        n = ctx.n.value
        p = ctx.p.value
        s = ctx.s.value if ctx.s else None
        ctx.value = dict(name = n, properties = p, signal = s)

    def exitFrame_kind(self, ctx):
        text = ctx.v.text
        ctx.value = text

    def exitFrame_name(self, ctx):
        name = ctx.i.value
        ctx.value = name

    def exitFrame_properties(self, ctx):
        """
    'length' '=' l = intValue ';'
    ('min_period' '=' minValue = intValue 'ms' ';')?
    ('max_period' '=' maxValue = intValue 'ms' ';')?
    ('event_triggered_frame' '=' etf = identifierValue)?
        """

    def exitSignal_definition(self, ctx):
        ctx.value = [x.value for x in ctx.items]

    def exitSignal_definition(self, ctx):
        n = ctx.n.value
        p = ctx.p.value
        ctx.value = dict(name = n, properties = p)

    def exitSignal_name(self, ctx):
        name = ctx.i.value
        ctx.value = name

    def exitSignal_properties(self, ctx):
        init = ctx.init.value
        s = ctx.s.value
        o = ctx.o.value
        e = ctx.e.value if ctx.e else None
        ctx.value = dic(initValue = init, size = s, offset = o, encoding = e)

    def exitInit_value(self, ctx):
        scalar = ctx.s.value if ctx.s else None
        array = ctx.a.value if ctx.a else None
        ctx.value = OrderedDict(scalar = scalar, array = array)

    def exitInit_value_scalar(self, ctx):
        ctx.value = ctx.i.value

    def exitInit_value_array(self, ctx):
        ctx.value = [x.value for x in ctx.vs]

    def exitEncoding_definition(self, ctx):
        ctx.value = [x.value for x in ctx.items]

    def exitEncoding_definition_entry(self, ctx):
        name = ctx.name.value
        items = [x.value for x in ctx.items]
        ctx.value = dict(name = name, values = items)

    def exitEncoding_definition_value(self, ctx):
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

    def exitEncoding_name(self, ctx):
        ctx.value = ctx.i.value

    def exitLogical_value(self, ctx):
        s = ctx.s.value
        t = ctx.t.value if ctx.t else None
        ctx.value = dict(signal = s, text = t)

    def exitPhysical_range(self, ctx):
        #'physical_value' ',' minValue = min_value ',' maxValue = max_value ',' s = scale ',' o = offset (',' t = text_info)? ';'
        minValue = ctx.minValue.value
        maxValue = ctx.maxValue.value
        s = ctx.s.value
        o = ctx.o.value
        t = ctx.t.value if ctx.t else None
        ctx.value = dict(min = minValue, max = maxValue, scale = s, offset = o, text = t)

    def exitBcd_value(self, ctx):
        pass

    def exitAscii_value(self, ctx):
        pass

    def exitSignal_value(self, ctx):
        ctx.value = ctx.n.value

    def exitMin_value(self, ctx):
        ctx.value = ctx.n.value

    def exitMax_value(self, ctx):
        ctx.value = ctx.n.value

    def exitScale(self, ctx):
        ctx.value = ctx.n.value

    def exitOffset(self, ctx):
        ctx.value = ctx.n.value

    def exitText_info(self, ctx):
        ctx.value = ctx.t.value

    def exitStatus_management(self, ctx):
        r = ctx.r.value
        values = [x.value for x in ctx.values] if ctx.values else []
        ctx.value = dict(responseError = r, faultStateSignals = values)

    def exitPublished_signal(self, ctx):
        pass

    def exitFree_text_definition(self, ctx):
        text = ctx.f.value
        ctx.value = text

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

