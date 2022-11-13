negtab = {'1':'0','0':'1'}
distab = {'11':'1','10':'1','01':'1','00':'0'}
contab = {'11':'1','10':'0','01':'0','00':'0'}

def mnegation(wff,interpretation):
    if wff[0] == '1':
        n = '1'
    elif wff[0] == '0':
        n = '0'
    else:
        if wff[0][0] == "-":
            n = mnegation(wff[0][1:],interpretation)
            return negtab[n]
        elif wff[0][0] == "*":
            n = mconjunction(wff[0][1:],interpretation)
            return negtab[n]
        elif wff[0][0] == "+":
            n = mdisjunction(wff[0][1:],interpretation)
            return negtab[n]
        else:
            if interpretation[wff[0]] == True:
                n = '1'
            if interpretation[wff[0]] == False:
                n = '0'
    return negtab[n]

def mconjunction(wff,interpretation):
    if wff[0][0] == '1':
        c = '1'
    elif wff[0][0] == '0':
        c = '0'
    else:
        if wff[0][0] == "-":
            c = mnegation(wff[0][1:],interpretation)
            return contab[c+meaning(wff[1],interpretation)]
        elif wff[0][0] == "*":
            c = mconjunction(wff[0][1:],interpretation)
            return contab[c+meaning(wff[1],interpretation)]
        elif wff[0][0] == "+":
            c = mdisjunction(wff[0][1:],interpretation)
            return contab[c+meaning(wff[1],interpretation)]
        else:
            if interpretation[wff[0][0]] == True:
                c = '1'
            if interpretation[wff[0][0]] == False:
                c = '0'
    return contab[c+meaning(wff[0][1],interpretation)]

def mdisjunction(wff,interpretation):
    if wff[0][0] == '1':
        d = '1'
    elif wff[0][0] == '0':
        d = '0'
    else:
        if wff[0][0] == "-":
            d = mnegation(wff[0][1:],interpretation)
            return distab[d+meaning(wff[1],interpretation)]
        elif wff[0][0] == "+":
            d = mconjunction(wff[0][1:],interpretation)
            return distab[d+meaning(wff[1],interpretation)]
        elif wff[0][0] == "+":
            d = mdisjunction(wff[0][1:],interpretation)
            return distab[d+meaning(wff[1],interpretation)]
        else:
            if interpretation[wff[0][0]] == True:
                d = '1'
            if interpretation[wff[0][0]] == False:
                d = '0'
    return distab[d+meaning(wff[0][1],interpretation)]

def meaning(wff,interpretation):
    if wff[0] == '1':
        x = '1'
    elif wff[0] == '0':
        x = '0'
    else:
        if wff[0] == "-":
            x = mnegation(wff[1:],interpretation)
        elif wff[0] == "*":
            x = mconjunction(wff[1:],interpretation)
        elif wff[0] == "+":
            x = mdisjunction(wff[1:],interpretation)
        else:
            if interpretation[wff] == True:
                x = '1'
            if interpretation[wff] == False:
                x = '0'
    return x

# print(meaning('1',{'P1':False}))
# print(meaning('P1',{'P1':False}))
# print(meaning(['-','P1'],{'P1':False}))
# print(meaning(['*',['P1','1']],{'P1':False}))
# print(meaning(['+',['P1','1']],{'P1':False}))
# print(meaning(['+',['P1',['-','1']]],{'P1':False}))
# print(meaning(['*',['+',['P1',['-','1']]],'1'],{'P1':True}))
# print(meaning(['-',['*',['P1',['-','P2']]]],{'P1':True,'P2':False}))
    
def demorgan(wff):
    x = wff[0:]
    if len(wff) > 1:
        x = demorganhelp(wff)
        if len(x) == 2:
            return x
        else:
            return [x]
    else:
        return x

def demorganhelp(wff):
    if wff[0] == "-":
        x = demorganneg(wff)
    elif wff[0] == "*":
        x = ['*']+[demorgancondis(wff[1])]
    elif wff[0] == "+":
        x = ['+']+[demorgancondis(wff[1])]
    else:
        x = [wff]
    return x

def demorganneg(wff):
    n = wff[0:]

    if wff[1][0] == '+':
        z1 = demorganhelp(wff[1][1][0])[0]
        z2 = demorganhelp(wff[1][1][1])[0]
        n[0] = '*'
        if z1 == '-' or z1 == '+' or z1 == '*':
            x = [demorganhelp(['-']+[demorganhelp(wff[1][1][0])])]
        else:
            x = [demorganhelp(['-']+demorganhelp(wff[1][1][0]))]
        if z2 == '-' or z2 == '+' or z2 == '*':
            y = [demorganhelp(['-']+[demorganhelp(wff[1][1][1])])]
        else:
            y = [demorganhelp(['-']+demorganhelp(wff[1][1][1]))]
        n[1] = x+y

    elif wff[1][0] == '*':
        z1 = demorganhelp(wff[1][1][0])[0]
        z2 = demorganhelp(wff[1][1][1])[0]
        n[0] = '+'
        if z1 == '-' or z1 == '+' or z1 == '*':
            x = [demorganhelp(['-']+[demorganhelp(wff[1][1][0])])]
        else:
            x = [demorganhelp(['-']+demorganhelp(wff[1][1][0]))]
        if z2 == '-' or z2 == '+' or z2 == '*':
            y = [demorganhelp(['-']+[demorganhelp(wff[1][1][1])])]
        else:
            y = [demorganhelp(['-']+demorganhelp(wff[1][1][1]))]
        n[1] = x+y  

    return n

def demorgancondis(wff):

    if demorganhelp(wff[0])[0] == '-':
        x = [demorganhelp(wff[0])]
    elif demorganhelp(wff[0])[0] == '*':
        x = [demorganhelp(wff[0])]
    elif demorganhelp(wff[0])[0] == '+':
        x = [demorganhelp(wff[0])]
    else:
        x = demorganhelp(wff[0])

    if demorganhelp(wff[1])[0] == '-':
        y = [demorganhelp(wff[1])]
    elif demorganhelp(wff[1])[0] == '*':
        y = [demorganhelp(wff[1])]
    elif demorganhelp(wff[1])[0] == '+':
        y = [demorganhelp(wff[1])]
    else:
        y = demorganhelp(wff[1])

    return x + y

# print(demorganhelp('a'))
# print(demorganhelp(['-','a']))
# print(demorganhelp(['*',['a','b']]))
# print(demorganhelp(['-',['-','a']]))
# print(demorganhelp(['-',['-',['-','a']]]))
# print(demorganhelp(['-',['+',['a','b']]]))
# print(demorganhelp(['*',[['-',['-','a']],['+',[['-','a'],'b']]]]))
# print(demorganhelp(['-',['+',[['-',['+',['a','b']]],'b']]]))
# print(demorganhelp(['-',['*', [['+', [['-', ['-', 'a']], ['-', ['-', 'b']]]], ['-', 'b']]]]))
# print('*'*100)


def dne(wff):
    x = wff[0:]
    if len(wff) > 1:
        x = dnehelp(wff)
        if len(x) == 2:
            return x
        else:
            return [x]
    else:
        return x

def dnehelp(wff):
    x = wff[0:]
    if wff[0] == '-':
        if wff[1][0] == '-':
            x = dnehelp(wff[1][1])
        if wff[1][0] == '+':
            x = [wff[0]] + [dnehelp(wff[1])]
        if wff[1][0] == '*':
            x = [wff[0]] + [dnehelp(wff[1])]
    if wff[0] == '+':
        x = [wff[0]] + [[dnehelp(wff[1][0])] + [dnehelp(wff[1][1])]]
    if wff[0] == '*':
        x = [wff[0]] + [[dnehelp(wff[1][0])] + [dnehelp(wff[1][1])]] 
    return x

# print(dne(['a']))
# print(dne(['-',['-','a']]))
# print(dne(['-',['-',['-','a']]]))
# print(dne(['-',['-',['-',['-','a']]]]))
# print(dne(['+',[['-',['-','a']],'b']]))
# print(dne(['*', [['+', [['-', ['-', 'a']], ['-', ['-', 'b']]]], ['-', 'b']]]))
# print(dne(['-',['*', [['+', [['-', ['-', 'a']], ['-', ['-', 'b']]]], ['-', 'b']]]]))


def connorm(wff):
    x = wff[0:]

    if wff[0] == '+':
        if wff[1][0][0] == '*':
            if wff[1][1][0] == '*':
                x[0] = '*'
                x[1] = [connorm(['+']+[[wff[1][0][1][0]]+[wff[1][1]]])] + [connorm(['+']+[[wff[1][0][1][1]]+[wff[1][1]]])]
            else:
                x[0] = '*'
                x[1] = [connorm(['+']+[[wff[1][0][1][0]]+[wff[1][1]]])] + [connorm(['+']+[[wff[1][0][1][1]]+[wff[1][1]]])]
            return x
        if wff[1][1][0] == '*':
            x[0] = '*'
            x[1] = [connorm(['+']+[[wff[1][0]]+[wff[1][1][1][0]]])] + [connorm(['+']+[[wff[1][0]]+[wff[1][1][1][1]]])]
        return x

    if wff[0] == '*':
        x[0] = '*'
        x[1] = [connorm(x[1][0])] + [connorm(x[1][1])]
        return x

    return x

# print(connorm(['+',[['*',['a','b']],'c']]))
# # output:     ['*',[['+',['a','c']],['+',['b','c']]]]
# print(connorm(['+',['a',['*',['b','c']]]]))
# # output:     ['*',[['+',['a','b'],['+',['a','c']]]]
# print(connorm(['+',[['*',['a','b']],['*',['c','d']]]]))
# # output:     ['*', [['*', [['+', ['a', 'c']], ['+', ['a', 'd']]]], ['*', [['+', ['b', 'c']], ['+', ['b', d'']]]]]

# print(connorm(['+',[['+',['a','b']],['*',['c','d']]]]))
# # output:     ['*', [['+', [['+', ['a', 'b']], 'c']], ['+', [['+', ['a', 'b']], 'd']]]]

# print(connorm(['*',[['+',[['*',['a','b']],['*',['c','d']]]],'e']]))
# print(connorm(['*',[['+',[['*',[['-','a'],'b']],['*',['c','d']]]],'e']]))

def sep(wff):
    x = wff[0:]
    if x[0] == '*':
        x = sephelp(wff)
        return x
    if x[0] == '-':
        return [x]
    else:
        return x

def sephelp(wff):
    x = wff[0:]
    if x[0] == '*':
        y1 = sephelp(wff[1][0])
        y2 = sephelp(wff[1][1])
        y3 = y1 + y2
    elif x[0] == '+':
        y3 = [x]
    else:
        y3 = [x]
    return y3

# print(connorm(['+',[['*',['a','b']],'c']]))
# print(sep(connorm(['+',[['*',['a','b']],'c']])))
# print('*'*100)
# print(sep(connorm(['+',[['*',['a','b']],['*',['c','d']]]])))
# print(connorm(['+',[['*',['a','b']],['*',['c','d']]]]))
# print('*'*100)
# print(connorm(['*',[['+',[['*',['a','b']],['*',['c','d']]]],'e']]))
# print(canonical(['*',[['+',[['*',['a','b']],['*',['c','d']]]],'e']]))


# print(canonical(['a']))
# print(canonical(['-','a']))
# print(canonical(['*',['a','b']]))
# print(canonical(['-',['-','a']]))
# print(canonical(['-',['-',['-','a']]]))
# print(canonical(['-',['+',['a','b']]]))
# print(canonical(['*',[['-',['-','a']],['+',[['-','a'],'b']]]]))
# print(canonical(['-',['*',[['-',['*',['a','b']]],'b']]]))
# print(canonical(['-',['*', [['+', [['-', ['-', 'a']], ['-', ['-', 'b']]]], ['-', 'b']]]]))

# print('*'*100)

# print(connorm(['+',[['*',['a','b']],'c']]))
# print(sep(connorm(['+',[['*',['a','b']],'c']])))
# # output:     ['*',[['+',['a','c']],['+',['b','c']]]]
# print(connorm(['+',['a',['*',['b','c']]]]))
# print(sep(connorm(['+',['a',['*',['b','c']]]])))
# # output:     ['*',[['+',['a','b'],['+',['a','c']]]]
# print(connorm(['+',[['*',['a','b']],['*',['c','d']]]]))
# print(sep(connorm(['+',[['*',['a','b']],['*',['c','d']]]])))
# # output:     ['*', [['*', [['+', ['a', 'c']], ['+', ['a', 'd']]]], ['*', [['+', ['b', 'c']], ['+', ['b', d'']]]]]
# print(connorm(['+',[['+',['a','b']],['*',['c','d']]]]))
# print(sep(connorm(['+',[['+',['a','b']],['*',['c','d']]]])))
# # output:     ['*', [['+', [['+', ['a', 'b']], 'c']], ['+', [['+', ['a', 'b']], 'd']]]]
# print(connorm(['*',[['+',[['*',['a','b']],['*',['c','d']]]],'e']]))
# print(sep(connorm(['*',[['+',[['*',['a','b']],['*',['c','d']]]],'e']])))

# print(connorm(['*',[['+',[['*',[['-','a'],'b']],['*',['c','d']]]],'e']]))
# print(sep(connorm(['*',[['+',[['*',[['-','a'],'b']],['*',['c','d']]]],'e']])))


def orcomb(lst):
    x = lst[0:]
    nlst = []
    for i in x:
        i = orcombhelp(i)
        nlst += [i]
    return orcombclean(nlst)

def orcombhelp(lst):
    x = lst[0:]
    if x[0] == '+':
        if x[1][0][0] == '+' and x[1][1][0] == '+':
            x[1] = [orcombhelp(x[1][0][1][0])] + [orcombhelp(x[1][0][1][1])] + [orcombhelp(x[1][1][1][0])] + [orcombhelp(x[1][1][1][1])]
        elif x[1][0][0] == '+':
            x[1] = [orcombhelp(x[1][0][1][0])] + [orcombhelp(x[1][0][1][1])] + [orcombhelp(x[1][1])]
        elif x[1][1][0] == '+':
            x[1] = [orcombhelp(x[1][1][1][0])] + [orcombhelp(x[1][1][1][1])] + [orcombhelp(x[1][0])]
    if x[0] == '-':
        return [x]
    return x

def orcombclean(lst):
    x = lst[0:]
    nlst = []
    for i in x:
        ilst = []
        if i[0] == '+':
            for j in i[1]:
                if j[0] == '+':
                    for k in j[1]:
                        if k[0] == '-':
                            ilst += [k]
                        else:
                            ilst += k
                elif j[0] == '-':
                    ilst += [j]
                else:
                    ilst += j
        else:
            ilst += i
        nlst += [ilst]
    return nlst


# print(connorm(['+',[['+',['a','b']],['*',['c','d']]]]))
# print(sep(connorm(['+',[['+',['a','b']],['*',['c','d']]]])))
# print(orcomb(sep(connorm(['+',[['+',['a','b']],['*',['c','d']]]]))))
# print(orcomb([['+', [['+', ['a', 'b']], 'c']], ['+', [['+', ['a', 'b']], 'd']]]))
# print(orcomb([['+', [['+', ['a', 'b']], ['+',['c','d']]]], ['+', [['+', ['a', 'b']], 'd']],'e']))
# print(orcomb([['+', [['+', [['+',[['+',[['-','a'],'w']],'x']], ['-','b']]], ['+',['c','d']]]], ['+', [['+', ['a', 'b']], 'd']],['-','e']]))
# print(orcomb([['+',['a','b']],['-','a']]))

    
def canonical(wff):
    return orcomb(sep(connorm(dne(demorgan(wff)))))

# print(canonical(['a']))
# print(canonical(['-','a']))
# print(canonical(['*',['a','b']]))
# print(canonical(['-',['-','a']]))
# print(canonical(['-',['-',['-','a']]]))
# print(canonical(['-',['+',['a','b']]]))
# print(canonical(['*',[['-',['-','a']],['+',[['-','a'],'b']]]]))
# print(canonical(['-',['*',[['-',['*',['a','b']]],'b']]]))
# print(canonical(['-',['*', [['+', [['-', ['-', 'a']], ['-', ['-', 'b']]]], ['-', 'b']]]]))


               
def resthepro(premise,goal):
    x = canonical(premise)
    neggoal = []
    if len(goal) > 1:
        print("Surprise")
        if goal[0] == '-':
            neggoal = ['-'] + [i]
            y = canonical(neggoal)
        else:
            for i in goal:
                    neggoal += canonical(['-'] + [i])
            y = neggoal
    else:
        neggoal = ['-'] + goal
        y = canonical(neggoal)

    f,c,u = y[0],x[0],[]
    if len(x) > 1 and len(y) == 1:
        q = x[1:]
    if len(x) > 1 and len(y) > 1:
        q = x[1:] + y[1:]
    if len(x) == 1 and len(y) == 1:
        q = []
    if len(x) == 1 and len(y) > 1:
        q = y[1:]
    print(f)
    print(c)
    print(q)
    print(u)
    print('*'*50)
    return reshelp(f,c,q,u,index = 0)

def reshelp(focus,comp,queue,unsuc,index):
    if index > len(queue) + 2:
        return "no contradiction"
        
    while True:
        for e1 in focus:
            for e2 in comp:
                if e1[0] == '-':
                    if e1[1] == e2:
                        nclause = resolve(focus,comp,e1,e2)
                        if nclause == []:
                            return "contradiction"
                        else:
                            if len(queue) > 1:
                                focus,comp,queue = nclause, queue[0], queue[1:]
                            elif len(queue) == 1:
                                focus,comp,queue = nclause, queue[0], []
                            else:
                                focus,comp,queue,unsuc = nclause, unsuc[0], unsuc[1:], []
                            return reshelp(focus,comp,queue,unsuc,index=0)    
                elif e2[0] == '-':
                    if e2[1] == e1:
                        nclause = resolve(focus,comp,e1,e2)
                        if nclause == []:
                            return "contradiction"
                        else:
                            if len(queue) > 1:
                                focus,comp,queue = nclause, queue[0], queue[1:]
                            elif len(queue) == 1:
                                focus,comp,queue = nclause, queue[0], []
                            else:
                                focus,comp,queue,unsuc = nclause, unsuc[0], unsuc[1:], []
                            return reshelp(focus,comp,queue,unsuc,index=0)

        if len(queue) > 1:
            unsuc,comp,queue = unsuc+[comp], queue[0], queue[1:]
            # print(focus)
            # print(comp)
            # print(queue)
            # print(unsuc)
            # print('*'*50)
            return reshelp(focus,comp,queue,unsuc,index)
        elif len(queue) == 1:
            unsuc,comp,queue = unsuc+[comp], queue[0], []
            # print(focus)
            # print(comp)
            # print(queue)
            # print(unsuc)
            # print('*'*50)
            return reshelp(focus,comp,queue,unsuc,index)
        else:
            if len(unsuc) > 2:
                focus,comp,queue,unsuc = unsuc[0], unsuc[1], unsuc[2:] + [focus] + [comp], []
            elif len(unsuc) == 2:
                focus,comp,queue,unsuc = unsuc[0], unsuc[1], [focus] + [comp], []
            elif len(unsuc) == 1:
                focus,comp,queue,unsuc = comp, unsuc[0], [focus], []
            # print(focus)
            # print(comp)
            # print(queue)
            # print(unsuc)
            # print('*'*50)
            return reshelp(focus,comp,queue,unsuc,index+1)

    
def resolve(clause1,clause2,element1,element2):
    nlst = []
    for i in clause1:
        if i != element1:
            nlst += [i]
    for j in clause2:
        if j != element2:
            nlst += [j]
    return nlst

# q = [['e'], ['a', 'd'], ['b', 'c'], ['b', 'd'], [['-', 'e']]]
# r = [['a', 'c']]
# print(resthepro(q,r))

# q1 = [['e'], ['a', 'd'], ['b', 'c'], ['b', 'd'], [['-', 'f']]]
# r1 = [['a', 'c']]
# print(resthepro(q1,r1))

# p = [['a',['-','b'],['-','c']],['b'],['c',['-','d'],['-','e']],['e','f'],['d'],[['-','f']]]
# g = [['-','a']]
# print(resthepro(p,g))

# p1 = [['a',['-','b'],['-','c']],['b'],['c',['-','d'],['-','e']],['e','f'],['d'],[['-','f']]]
# g1 = [['-','x']]
# print(resthepro(p1,g1))

# p = [[['-','a'],['-','b'],['-','c']],['b'],['c',['-','d'],['-','e']],['e','f'],['d'],[['-','f']]]
# g = ['a']
# print(resthepro(p,g))
# print(canonical(['*',[['+',[['*',['a','b']],['*',['c','d']]]],['-','e']]]))

print(resthepro(['*',[['+',[['*',['a','b']],['*',['c','d']]]],['-','e']]],[['-','e']]))

# WORKS RIGHT NOW WITH ENTRIES OF MULTIPLE PREMISES AND ONLY ONE GOAL
# FIX SO IT WORKS WITH ENTRIES OF ONLY ONE PREMISE AND ENTRIES WITH WITH MORE THAN ONE GOAL