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
    return And(clauses)

def cleanTerm2(tr, at):
    clauses = []
    for k in tr.lst:
        print "curr: ",k
        if isinstance(k, Literal):
            if not k.__eq__(at):
                clauses.append(k)
        elif isinstance(k, Not):
            if not k.__eq__(at):
                clauses.append(k)
        elif k == F or k == T:
            if k.__eq__(F):
                return False
        else:
            #print "We have OR",k,at,k.lst
            if at not in k.lst:
                #print "We search OR"
                if Not(at).simplify() in k.lst:
                    #print "searching in list: ",k.lst," for ",Not(at).simplify()
                    ctype = k.getClass()
                    elems = []
                    for k2 in k.lst:

                        # print k2,Not(at),k2!=Not(at),k2==Not(at)
                        if not Not(at).simplify().__eq__(k2):
                            # print k2
                            elems.append(k2)
                    if elems.__len__() == 1:
                        clauses.append(elems[0])
                    else:
                        clauses.append(ctype(elems))
                else:
                    clauses.append(k)
    return And(clauses)
# Unit propagate
#t = And(Or(2, 3), Or(Not(1), 2), 1, Or(7, 8))
#t=And(1,Or(1,2))
#t2 = [3]
#for k in t.lst:
#    t2.append(k)
#t2=And(t2)
#print t
# while True:
#a = getAtom(t)
#print "selected: ", a
# if a == None:
# break
#t = cleanTerm(t, a)
#print "t: ", t
#print t2
# print "end of propagation: ",t
# a=getAtom(t)
# print a
# print t
# h = cleanTerm(t,a)
# print h
#t=And(Or(1,2),Or(Not(1),3),Or(Not(1),Not(2),Not(3)),Not(1))
#a = getAtom(t)
#print a
#t = cleanTerm2(t, a)
#print t
print Or(1,Not(2),3)
