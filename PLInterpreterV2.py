def conjunction(x,y):
    x,y = int(x),int(y)
    return min(x,y)

def negation(x):
    x = int(x)
    return x*-1+1

def disjunction(x,y):
    x,y = int(x),int(y)
    return max(x,y)

def implication(x,y):
    return int(x <= y)

def biconditional(x,y):
    return int(x == y)

#************************************************************************

def meaning(wff,interpretation):
    if type(wff[0]) == int:
        return bool(wff[0])
    if wff[0] == "*":
        x = meaning(wff[1],interpretation)
        y = meaning(wff[2],interpretation)
        return bool(conjunction(x,y))
    if wff[0] == "+":
        x = meaning(wff[1],interpretation)
        y = meaning(wff[2],interpretation)
        return bool(disjunction(x,y))
    if wff[0] == "-":
        x = meaning(wff[1],interpretation)
        return bool(negation(x))
    for i in interpretation.keys():
        if wff == i:
            return interpretation[i]

#*****************************************************************

def meaning_c(wff, interpretation):
    x = len(wff[1])
    for i in interpretation.keys():
        if wff[1][x-1] == i:
            a = interpretation[i]
        else:
            a = bool(wff[1][x-1])
    if x == 2:
        a = negation(a)
    y = len(wff[2])
    for i in interpretation.keys():
        if wff[2][y-1] == i:
            b = interpretation[i]
        else:
            b = bool(wff[2][y-1])
    if y == 2:
        b = negation(b)
    return bool(conjunction(a,b))

def meaning_d(wff, interpretation):
    x = len(wff[1])
    for i in interpretation.keys():
        if wff[1][x-1] == i:
            a = interpretation[i]
        else:
            a = bool(wff[1][x-1])
    if x == 2:
        a = negation(a)
    y = len(wff[2])
    for i in interpretation.keys():
        if wff[2][y-1] == i:
            b = interpretation[i]
        else:
            b = bool(wff[2][y-1])
    if y == 2:
        b = negation(b)
    return bool(disjunction(a,b))

def meaning_i(wff, interpretation):
    x = len(wff[1])
    for i in interpretation.keys():
        if wff[1][x-1] == i:
            a = interpretation[i]
        else:
            a = bool(wff[1][x-1])
    if x == 2:
        a = negation(a)
    y = len(wff[2])
    for i in interpretation.keys():
        if wff[2][y-1] == i:
            b = interpretation[i]
        else:
            b = bool(wff[2][y-1])
    if y == 2:
        b = negation(b)
    return bool(implication(a,b))

print(meaning(['*',['-','P1'],[1]],{'P1':True}))
print(meaning_c(['*',['-','P1'],[1]],{'P1':True}))
print(meaning_d(['+',['-','P1'],[1]],{'P1':True}))
print(meaning_i(['->',['-','P1'],[1]],{'P1':True}))
