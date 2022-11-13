negtab = {'1':'0','0':'1'}
distab = {'11':'1','10':'1','01':'1','00':'0'}
contab = {'11':'1','10':'0','01':'0','00':'0'}

def v4mnegation(wff,interpretation):
    if wff[0] == '1':
        n = '1'
    elif wff[0] == '0':
        n = '0'
    else:
        if wff[0][0] == "-":
            n = v4mnegation(wff[0][1:],interpretation)
            return negtab[n]
        elif wff[0][0] == "*":
            n = v4mconjunction(wff[0][1:],interpretation)
            return negtab[n]
        elif wff[0][0] == "+":
            n = v4mdisjunction(wff[0][1:],interpretation)
            return negtab[n]
        else:
            if interpretation[wff[0]] == True:
                n = '1'
            if interpretation[wff[0]] == False:
                n = '0'
    return negtab[n]

def v4mconjunction(wff,interpretation):
    if wff[0][0] == '1':
        c = '1'
    elif wff[0][0] == '0':
        c = '0'
    else:
        if wff[0][0] == "-":
            c = v4mnegation(wff[0][1:],interpretation)
            return contab[c+v4meaning(wff[1],interpretation)]
        elif wff[0][0] == "*":
            c = v4mconjunction(wff[0][1:],interpretation)
            return contab[c+v4meaning(wff[1],interpretation)]
        elif wff[0][0] == "+":
            c = v4mdisjunction(wff[0][1:],interpretation)
            return contab[c+v4meaning(wff[1],interpretation)]
        else:
            if interpretation[wff[0][0]] == True:
                c = '1'
            if interpretation[wff[0][0]] == False:
                c = '0'
    return contab[c+v4meaning(wff[0][1],interpretation)]

def v4mdisjunction(wff,interpretation):
    if wff[0][0] == '1':
        d = '1'
    elif wff[0][0] == '0':
        d = '0'
    else:
        if wff[0][0] == "-":
            d = v4mnegation(wff[0][1:],interpretation)
            return distab[d+v4meaning(wff[1],interpretation)]
        elif wff[0][0] == "+":
            d = v4mconjunction(wff[0][1:],interpretation)
            return distab[d+v4meaning(wff[1],interpretation)]
        elif wff[0][0] == "+":
            d = v4mdisjunction(wff[0][1:],interpretation)
            return distab[d+v4meaning(wff[1],interpretation)]
        else:
            if interpretation[wff[0][0]] == True:
                d = '1'
            if interpretation[wff[0][0]] == False:
                d = '0'
    return distab[d+v4meaning(wff[0][1],interpretation)]

def v4meaning(wff,interpretation):
    if wff[0] == '1':
        x = '1'
    elif wff[0] == '0':
        x = '0'
    else:
        if wff[0] == "-":
            x = v4mnegation(wff[1:],interpretation)
        elif wff[0] == "*":
            x = v4mconjunction(wff[1:],interpretation)
        elif wff[0] == "+":
            x = v4mdisjunction(wff[1:],interpretation)
        else:
            if interpretation[wff] == True:
                x = '1'
            if interpretation[wff] == False:
                x = '0'
    return x

print(v4meaning('1',{'P1':False}))
print(v4meaning('P1',{'P1':False}))
print(v4meaning(('-','P1'),{'P1':False}))
print(v4meaning(('*',('P1','1')),{'P1':False}))
print(v4meaning(('+',('P1','1')),{'P1':False}))
print(v4meaning(('+',('P1',('-','1'))),{'P1':False}))
print(v4meaning(('*',('+',('P1',('-','1'))),'1'),{'P1':True}))
print(v4meaning(('-',('*',('P1',('-','P2')))),{'P1':True,'P2':False}))
