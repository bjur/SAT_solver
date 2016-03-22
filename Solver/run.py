from sat import *
import sys
from read_file import *

input_file = readDimacs(sys.argv[1])

print("Reading *.cnf file")
print("Finding solution")
#sol=solve(And(1,Not(1)),[])
sol = solve(input_file,[])
if sol == False:
    print "No solution found"
else:
    bs = buildSoultion(sol)
    h=input_file.evaluate(bs)
    print "Solution was found: ", h
    if h:
        print "Solution: ",bs
        print "Solution evaluation: ",h
