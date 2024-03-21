# Import known RE functions from z3 into this namespace.

from z3 import (Re,
    InRe, # contained in R1
    Union, # "a" "b" "c" -> "abc". I'd call this concatenation but eh
    Diff, # R1 - R2
    Star, # "a*"
    Intersect, # R1 intersect R2
    Loop,      # "a{n,m}"
    Option,   # "a?"
    Full, # ".*"
    Plus, # "a+"
)