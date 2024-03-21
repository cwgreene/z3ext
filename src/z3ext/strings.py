import z3

def startswith(s, string):
    if type(string) == str:
        return z3.SubString(s, 0, len(string)) == string
    else:
        return z3.SubString(s, 0, z3.Length(string)) == string

def endswith(s, string):
    if type(string) == str:
        return z3.SubString(s, z3.Length(s) - len(string), z3.Length(s)) == string
    else:
        return z3.SubString(s, z3.Length(s) - z3.Length(string), z3.Length(s)) == string

# Proposed api:
# startswith

def StringExt(name):
    pass