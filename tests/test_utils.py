import z3
from z3ext import contained_in
from z3ext.strings import startswith

def test_contained_in():
    strings = ["bob", "joe", "sam"]
    full_string = z3.String("full_string")

    solver = z3.Solver()
    solver.add(startswith(full_string, "s"))
    solver.add(contained_in(full_string, strings))

    assert solver.check() == z3.sat
    m = solver.model()
    
    assert m[full_string] == "sam"