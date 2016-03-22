from propagate import *
from collections import Counter

def buildSoultion(sol):
    dictsol = {}
    for k in sol:
        if isinstance(k,Not):
            dictsol[int(Not(k).simplify().__str__())]=False
        else:
            dictsol[int(k.__str__())]=True
    return dictsol

def selectTerm(term):
    ts = []
    for k in term.lst:
        if isinstance(k,Literal) or isinstance(k,Not):
            ts.append(k)
        else:
            for k2 in k.lst:
                ts.append(k2)
    return Counter(ts).most_common()[0][0]

def addTerm(term,a):
    new = [a]
    for k in term.lst:
        new.append(k)
    return And(new)

def solve(term,solution):
    #Unit propagation
    while True:
        a = getAtom(term)
        #print "selected: ",a
        if a == None:
            break
        else:
            solution.append(a)
        term=cleanTerm2(term,a)
        #print "t: ",term
    print "end of up: ",term
    if term == T:
        return solution
        #return True
    elif term == F:
        return False
    #Assumption
    g = selectTerm(term)
    #print "assuming: ",g
    #print "term: ",term
    tpos = addTerm(term,g)
    possolve = solve(tpos,solution);
    if possolve == False:
        tneg = addTerm(term,Not(g))
        return solve(tneg,solution)
    else:
        return possolve
