from boolean import *


def getAtom(term):
    for elem in term.lst:
        if not isinstance(elem, Or):
            return elem
    return None


def cleanTerm(tr, at):
    clauses = []
    for k in tr.lst:
        if isinstance(k, Literal):
            if not k == at:
                clauses.append(k)
        elif isinstance(k, Not):
            print k
            if not k == at:
                clauses.append(k)
        elif k == F or k == T:
            print "boo"
            if k == F:
                return False
        else:
            if at not in k.lst:
                if Not(at) in k.lst:
                    ctype = k.getClass()
                    elems = []
                    for k2 in k.lst:
                        # print k2,Not(at),k2!=Not(at),k2==Not(at)
                        if not k2 == Not(at):
                            # print k2
                            elems.append(k2)
                    if elems.__len__() == 1:
                        clauses.append(elems[0])
                    else:
                        clauses.append(ctype(elems))
                else:
                    clauses.append(k)
    print "hi: ", clauses
    return And(clauses)


# Unit propagate
#t = And(Or(2, 3), Or(Not(1), 2), 1, Or(7, 8))
#print t
# while True:
#a = getAtom(t)
#print "selected: ", a
# if a == None:
# break
#t = cleanTerm(t, a)
#print "t: ", t
# print "end of propagation: ",t
# a=getAtom(t)
# print a
# print t
# h = cleanTerm(t,a)
# print h
