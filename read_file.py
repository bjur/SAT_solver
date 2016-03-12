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
                    clauses.append(And(ls))
    f.close()
    return Or(clauses)

t = readDimacs("dimacs_test_1")
print t
