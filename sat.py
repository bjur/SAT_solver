from boolean import *
from read_file import *
from propagate import *
from collections import Counter

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
        print "selected: ",a
        if a == None:
            break
        else:
            solution.append(a)
        term=cleanTerm2(term,a)
        print "t: ",term
    print "end of up: ",term
    if term == T:
        print solution
        return True
    elif term == F:
        return False
    #Assumption
    g = selectTerm(term)
    print "assuming: ",g
    #print "term: ",term
    tpos = addTerm(term,g)
    if solve(tpos,solution):
        return True
    else:
        tneg = addTerm(term,Not(g))
        return solve(tneg,solution)

    #print term
    #print solution

a = readDimacs("sudoku1cnf")
#a=And(Or(1,2),Or(Not(1),3),Or(Not(1),Not(2),Not(3)))
#print a
solve(a,[])
#k=selectTerm(a)
#print k
#print max(set(k), key=k.count)
#print Counter(k).most_common()[0][0]
