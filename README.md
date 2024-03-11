This contains useful extensions to z3.

In particular this defines the Logical BitVec, which
overrides the Left Shift Operator `>>` from being
by default Arithmetic Shift to being Logical Shift.

This makes it possible to directly pass in a BitVecL
into many python functions that are essentially operating
with unsigned numbers.
