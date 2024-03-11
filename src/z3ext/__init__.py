import z3

def BitVecL(name, bv, ctx=None):
    if isinstance(bv, z3.BitVecSortRef):
        ctx = bv.ctx
    else:
        ctx = z3.get_ctx(ctx)
        bv = z3.BitVecSort(bv, ctx)
    return BitVecLRef(z3.Z3_mk_const(ctx.ref(), z3.to_symbol(name, ctx), bv.ast), ctx)


class BitVecLRef(z3.BitVecRef):
   def __rshift__(self, o):
        return z3.LShR(self, o)
