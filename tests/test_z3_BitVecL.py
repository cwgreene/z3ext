import z3
from z3ext import BitVecL

def test_BitVecL():
    b = BitVecL("b", 64)
    s = z3.Solver()
    s.add(b==(2**64-1))
    s.add((b >> 1) & 2**63 == 0)
    assert s.check() == z3.sat

# This is for sanity checking
# That BitVecL and BitVec are different
def test_BitVec():
    b = z3.BitVec("b", 64)
    s = z3.Solver()
    s.add(b==(2**64-1))
    # The leading bit after the shift is not 0
    # as it needs to remain negative.
    s.add((b >> 1) & 2**63 == 0)
    assert s.check() == z3.unsat
