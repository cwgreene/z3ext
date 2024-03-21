import z3
from z3ext import contained_in, startswith, endswith

def test_contained_in():
    strings = ["bob", "joe", "sam"]
    full_string = z3.String("full_string")

    solver = z3.Solver()
    solver.add(startswith(full_string, "s"))
    solver.add(contained_in(full_string, strings))

    assert solver.check() == z3.sat
    m = solver.model()
    
    assert m[full_string] == "sam"


def test_startswith():
    s = z3.String("s")
    solver = z3.Solver()
    solver.add(startswith(s, "abc"))
    assert solver.check() == z3.sat
    m = solver.model()
    print(m)
    assert type(m[s].as_string()) == str
    assert m[s].as_string().startswith("abc")

    # Make sure Length can be controlled
    solver.add(z3.Length(s) == 5)
    assert solver.check() == z3.sat
    m = solver.model()
    assert m[s].as_string().startswith("abc")
    assert len(m[s].as_string()) == 5

def test_endswith():
    s = z3.String("s")
    solver = z3.Solver()
    solver.add(endswith(s, "abc"))
    assert solver.check() == z3.sat
    m = solver.model()
    print(m)
    assert type(m[s].as_string()) == str
    assert m[s].as_string().endswith("abc")

    # Make sure Length can be controlled
    solver.add(z3.Length(s) == 5)
    assert solver.check() == z3.sat
    m = solver.model()
    assert m[s].as_string().endswith("abc")
    assert len(m[s].as_string()) == 5

def test_string_startsends_symbol():
    s = z3.String("s")
    prefix = z3.String("prefix")
    suffix = z3.String("suffix")
    
    solver = z3.Solver()
    solver.add([endswith(s, suffix), startswith(s, prefix)])
    solver.add(z3.Length(s)==7)
    solver.add(z3.Length(prefix)==3)
    solver.add(z3.Length(suffix)==4)

    assert solver.check() == z3.sat
    m = solver.model()
    assert m[s].as_string() == m[prefix].as_string() + m[suffix].as_string()