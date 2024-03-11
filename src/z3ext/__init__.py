import z3

def BitVecL(name, bv, ctx=None):
    """Return a bit-vector constant named `name`. `bv` may be the number of bits of a bit-vector sort.
    If `ctx=None`, then the global context is used.

    >>> x  = BitVec('x', 16)
    >>> is_bv(x)
    True
    >>> x.size()
    16
    >>> x.sort()
    BitVec(16)
    >>> word = BitVecSort(16)
    >>> x2 = BitVec('x', word)
    >>> eq(x, x2)
    True
    """
    if isinstance(bv, z3.BitVecSortRef):
        ctx = bv.ctx
    else:
        ctx = z3.get_ctx(ctx)
        bv = z3.BitVecSort(bv, ctx)
    return BitVecLRef(z3.Z3_mk_const(ctx.ref(), z3.to_symbol(name, ctx), bv.ast), ctx)


class BitVecLRef(z3.BitVecRef):
   def __rshift__(self, o):
        return z3.LShR(self, o)
