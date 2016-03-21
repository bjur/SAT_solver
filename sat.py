from boolean import *
from read_file import *
from propagate import *

def solve(term,solution):
    #Unit propagation
    while True:
        a = getAtom(term)
        print "selected: ",a
        if a == None:
            break
        else:
            solution.append(a)
        term=cleanTerm(term,a)
        print "t: ",term
    print term
    print solution

a = readDimacs("sudoku1cnf")
print a
solve(a,[])