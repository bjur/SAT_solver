from boolean import *


def getAtom(term):
    for elem in term.lst:
        if not isinstance(elem, Or):
            return elem
    return None

def cleanTerm2(tr, at):
    clauses = []
    for k in tr.lst:
        if isinstance(k, Literal):
            if k != at:
                clauses.append(k)
        elif isinstance(k, Not):
            if k != at:
                clauses.append(k)
        elif k == F or k == T:
            if k != F:
                return False
        else:
            if at not in k.lst:
                if Not(at).simplify() in k.lst:
                    ctype = k.getClass()
                    elems = []
                    for k2 in k.lst:
                        if not Not(at).simplify().__eq__(k2):
                            elems.append(k2)
                    if elems.__len__() == 1:
                        clauses.append(elems[0])
                    else:
                        clauses.append(ctype(elems))
                else:
                    clauses.append(k)
    return And(clauses)
