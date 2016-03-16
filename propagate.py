from boolean import *

def getAtom(term):
    for elem in term.lst:
        if not isinstance(elem,Or):
            return elem
    return None

def cleanTerm(tr,at):
    clauses = []
    for k in tr.lst:
        if isinstance(k,Literal):
            if k!=at:
                clauses.append(k)
        elif isinstance(k,Not):
            if k != Not(at):
                clauses.append(k)
            else:
                return False
        elif k==F or k==T:
            if k==F:
                return False
        else:
            if at not in k.lst:
                if Not(at) in k.lst:
                    ctype = k.getClass()
                    elems = []
                    for k2 in k.lst:
                        #print k2,Not(at),k2!=Not(at),k2==Not(at)
                        if not k2 == Not(at):
                            #print k2
                            elems.append(k2)
                    if elems.__len__()==1:
                        clauses.append(elems[0])
                    else:
                        clauses.append(ctype(elems))
                else:
                    clauses.append(k)
    return And(clauses)

#t = And(Or(1,2),("v",1,2),1,Or(Not(1),2))
#for k in t.lst:
    #print k.__eq__(makeFormula(2))
    #print k.hasSubclause(2)
    #print k,isinstance(k, Not)
    #print k.simplify()
#print t
#print getAtom(t)
#print t
#print t
#Unit propagate
t = And(Or(2,3),Or(Not(1),2),1,("v",4),Or(7,8))
print t
while True:
    a = getAtom(t)
    print "selected: ",a
    if a == None:
        break
    t=cleanTerm(t,a)
    print "t: ",t
print "end of propagation: ",t
#a=getAtom(t)
#print a
#print t
#h = cleanTerm(t,a)
#print h