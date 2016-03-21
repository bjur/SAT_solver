from boolean import *

def readDimacs(filename):
    clauses = []
    with open(filename, "r") as f:
        for line in f:
            ls = line.split( )
            if ls[0] != 'c':
                if ls[-1] == '0':
                    ls.__delitem__(-1)
                    ls=map(int,ls)
                    mc = []
                    for k in ls:
                        if k<0:
                            mc.append(Not(abs(k)))
                        else:
                            mc.append(k)
                    clauses.append(Or(mc))
    f.close()
    return And(clauses).simplify()
