def negation(nlst):
    n = nlst
    if type(nlst[0]) != int:
        if nlst[0][0] == "not":
            n = negation(nlst[0][1:])
            return not n
        if nlst[0][0] == "and":
            n = conjunction(nlst[0][1:])
            return not n
        if nlst[0][0] == "or":
            n = disjunction(nlst[0][1:])
            return not n
    else:
        return not n[0]

def conjunction(clst):
    c = clst
    if type(clst[0]) != int:
        if clst[0][0] == "not":
            c = negation(clst[0][1:])
            return c and interpreter(clst[1])
        if clst[0][0] == "and":
            c = conjunction(clst[0][1:])
            return c and interpreter(clst[1])
        if clst[0][0] == "or":
            c = disjunction(clst[0][1:])
            return c and interpreter(clst[1])
    else:
        return c[0] and c[1]

def disjunction(dlst):
    d = dlst
    if type(dlst[0]) != int:
        if dlst[0][0] == "not":
            d = negation(dlst[0][1:])
            return d or interpreter(dlst[1])
        if dlst[0][0] == "and":
            d = conjunction(dlst[0][1:])
            return d or interpreter(dlst[1])
        if dlst[0][0] == "or":
            d = disjunction(dlst[0][1:])
            return d or interpreter(dlst[1])
    else:
        return d[0] or d[1]

def interpreter(xlst):
    x = xlst
    if type(xlst) != int:
        if xlst[0] == "not":
            x = negation(xlst[1:])
        if xlst[0] == "and":
            x = conjunction(xlst[1:])
        if xlst[0] == "or":
            x = disjunction(xlst[1:])
    return bool(x)

p = 0
q = 1
print(interpreter(["not",["not",["not",p]]]))
print(interpreter(["not",["and",["not",p],["not",q]]]))
print(interpreter(["not",["and",["or",["not", p],["not",q]],q]]))