import z3

class StringExtRef(z3.SeqRef):
    def startswith(self, s):
        return startswith(self, s)

    def endswith(self, s):
        return endswith(self, s)

    def length(self):
        return z3.Length(self)

def String(name, ctx = None):
    """Return a string constant named `name`. If `ctx=None`, then the global context is used.

    >>> x = String('x')
    """
    ctx = z3.get_ctx(ctx)
    return StringExtRef(z3.Z3_mk_const(ctx.ref(), z3.to_symbol(name, ctx), z3.StringSort(ctx).ast), ctx)
  

# I guess we could just use z3.PrefixOf for impl
def startswith(s : str | z3.SeqRef, string : str | z3.SeqRef):
    if type(string) == str:
        return z3.SubString(s, 0, len(string)) == string
    else:
        return z3.SubString(s, 0, z3.Length(string)) == string

# I guess we could just use z3.SuffixOf for impl
def endswith(s : str | z3.SeqRef, string : str | z3.SeqRef):
    if type(string) == str:
        return z3.SubString(s, z3.Length(s) - len(string), z3.Length(s)) == string
    else:
        return z3.SubString(s, z3.Length(s) - z3.Length(string), z3.Length(s)) == string
