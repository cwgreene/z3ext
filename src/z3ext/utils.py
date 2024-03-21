import z3

def contained_in(symbol, array):
    return z3.Or([symbol == s for s in array])