import z3
from z3ext.strings import startswith, endswith
from z3ext.strings import String

def test_startswith():
    s = z3.String("s")
    solver = z3.Solver()
    solver.add(startswith(s, "abc"))
    assert solver.check() == z3.sat
    m = solver.model()
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
    # be nice to say:
    #   's.endswith(suffix) and s.startswith(prefix)'
    #   'len(s) == 7'
    solver.add([endswith(s, suffix), startswith(s, prefix)])
    solver.add(z3.Length(s)==7)
    solver.add(z3.Length(prefix)==3)
    solver.add(z3.Length(suffix)==4)

    assert solver.check() == z3.sat
    m = solver.model()
    assert m[s].as_string() == m[prefix].as_string() + m[suffix].as_string()

def test_string_class():
    s = String("s")
    prefix = String("prefix")
    suffix = String("suffix")
    
    solver = z3.Solver()
    # test endswith, startswith
    solver.add([s.endswith(suffix), s.startswith(prefix)])
    
    # test length
    solver.add(s.length()==7)
    solver.add(prefix.length()==3)
    solver.add(suffix.length()==4)

    assert solver.check() == z3.sat
    m = solver.model()
    assert m[s].as_string() == m[prefix].as_string() + m[suffix].as_string()

    # Test contains
    solver.add(s.contains(prefix))
    solver.add(s.contains(suffix))
    assert solver.check() == z3.sat