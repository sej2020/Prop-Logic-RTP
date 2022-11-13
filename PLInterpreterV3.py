def conjunction(x,y):
    return min(x,y)

def negation(x):
    return 1-x

def disjunction(x,y):
    return max(x,y)

#************************************************************************************************************************************************************

#VERSION ONE - returns floats or integers. works for fuzzy logic. does not work for compositionality as-is, because input is of
#              different type than input. Idea is to work for ('*','P1','1') form of input.

def v1mconjunction(wff,interpretation):
    if wff[1] == '0':
        x = 0
    elif wff[1] == '1':
        x = 1
    else:
        x = interpretation[wff[1]]
    if wff[2] == '0':
        y = 0
    elif wff[2] == '1':
        y = 1
    else:
        y = interpretation[wff[2]]
    return conjunction(x,y)

def v1mdisjunction(wff,interpretation):
    if wff[1] == '0':
        x = 0
    elif wff[1] == '1':
        x = 1
    else:
        x = interpretation[wff[1]]
    if wff[2] == '0':
        y = 0
    elif wff[2] == '1':
        y = 1
    else:
        y = interpretation[wff[2]]
    return disjunction(x,y)

def v1mnegation(wff,interpretation):
    if wff[1] == '0':
        x = 0
    elif wff[1] == '1':
        x = 1
    else:
        x = interpretation[wff[1]]
    return negation(x)

#***************************************************************************************************************

#VERSION TWO - returns strings. Does not work for fuzzy logic. could work for larger compositional system.
#              intended for input of ('*','P1','1') form

def v2mconjunction(wff,interpretation):
    if wff[0] == '0':
        x = 0
    elif wff[0] == '1':
        x = 1
    else:
        x = interpretation[wff[0]]
    if wff[1] == '0':
        y = 0
    elif wff[1] == '1':
        y = 1
    else:
        y = interpretation[wff[1]]
    if conjunction(x,y) == 0:
        return '0'
    else:
        return '1'

def v2mdisjunction(wff,interpretation):
    if wff[0] == '0':
        x = 0
    elif wff[0] == '1':
        x = 1
    else:
        x = interpretation[wff[0]]
    if wff[1] == '0':
        y = 0
    elif wff[1] == '1':
        y = 1
    else:
        y = interpretation[wff[1]]
    if disjunction(x,y) == 0:
        return '0'
    else:
        return '1'

def v2mnegation(wff,interpretation):
    if wff[0] == '0':
        x = 0
    elif wff[0] == '1':
        x = 1
    else:
        x = interpretation[wff[0]]
    if negation(x) == 0:
        return '0'
    else:
        return '1'

def v2meaning(wff,interpretation):
    if wff[0] == '0':
        x = 0
    elif wff[0] == '1':
        x = 1
    elif wff[0] == "*":
            x = v2mconjunction(wff[1:],interpretation)
    elif wff[0] == "+":
            x = v2mdisjunction(wff[1:],interpretation)
    elif wff[0] == "-":
            x = v2mnegation(wff[1:],interpretation)
    return x

# print(v2meaning(('-','P1'),{'P1':True}))
# print(v2meaning(('*','0','1'),{'P1':True}))
# print(v2meaning(('+','P1','0'),{'P1':False}))

#******************************************************************************************************************************

#VERSION 3 - trying to create compositional system. input is strings in form ('+',('P1',('-','1'))). output is integer. could be converted to string easily.
# 		 it works right with all my tests, but something seems off

def v3mnegation(wff,interpretation):
    n = wff
    if wff[0] == '1':
        n = 1
    elif wff[0] == '0':
        n = 0
    else:
        if wff[0][0] == "-":
            n = v3mnegation(wff[0][1:],interpretation)
            return negation(n)
        if wff[0][0] == "*":
            n = v3mconjunction(wff[0][1:],interpretation)
            return negation(n)
        if wff[0][0] == "+":
            n = v3mdisjunction(wff[0][1:],interpretation)
            return negation(n)
        else:
            if interpretation[wff[0]] == True:
                n = 1
            if interpretation[wff[0]] == False:
                n = 0
    return negation(n)

def v3mconjunction(wff,interpretation):
    c = wff
    if wff[0][0] == '1':
        c = 1
    elif wff[0][0] == '0':
        c = 0
    else:
        if wff[0][0] == "-":
            c = v3mnegation(wff[0][1:],interpretation)
            return conjunction(c,v3meaning(wff[1],interpretation))
        if wff[0][0] == "*":
            c = v3mconjunction(wff[0][1:],interpretation)
            return conjunction(c,v3meaning(wff[1],interpretation))
        if wff[0][0] == "+":
            c = v3mdisjunction(wff[0][1:],interpretation)
            return conjunction(c,v3meaning(wff[1],interpretation))
        else:
            if interpretation[wff[0][0]] == True:
                c = 1
            if interpretation[wff[0][0]] == False:
                c = 0
    return conjunction(c,v3meaning(wff[0][1],interpretation))

def v3mdisjunction(wff,interpretation):
    d = wff
    if wff[0][0] == '1':
        d = 1
    elif wff[0][0] == '0':
        d = 0
    else:
        if wff[0][0] == "-":
            d = v3mnegation(wff[0][1:],interpretation)
            return disjunction(d,v3meaning(wff[1],interpretation))
        if wff[0][0] == "+":
            d = v3mconjunction(wff[0][1:],interpretation)
            return disjunction(d,v3meaning(wff[1],interpretation))
        if wff[0][0] == "+":
            d = v3mdisjunction(wff[0][1:],interpretation)
            return disjunction(d,v3meaning(wff[1],interpretation))
        else:
            if interpretation[wff[0][0]] == True:
                d = 1
            if interpretation[wff[0][0]] == False:
                d = 0
    return disjunction(d,v3meaning(wff[0][1],interpretation))

def v3meaning(wff,interpretation):
    x = wff
    if wff[0][0] == '1':
        x = 1
    elif wff[0][0] == '0':
        x = 0
    else:
        if wff[0] == "-":
            x = v3mnegation(wff[1:],interpretation)
        elif wff[0] == "*":
            x = v3mconjunction(wff[1:],interpretation)
        elif wff[0] == "+":
            x = v3mdisjunction(wff[1:],interpretation)
        else:
            if interpretation[wff] == True:
                x = 1
            if interpretation[wff] == False:
                x = 0
    return x

# print(v3meaning('1',{'P1':False}))
# print(v3meaning('P1',{'P1':False}))
# print(v3meaning(('-','P1'),{'P1':False}))
# print(v3meaning(('*',('P1','1')),{'P1':False}))
# print(v3meaning(('+',('P1','1')),{'P1':False}))
# print(v3meaning(('+',('P1',('-','1'))),{'P1':False}))
# print(v3meaning(('*',('+',('P1',('-','1'))),'1'),{'P1':True}))