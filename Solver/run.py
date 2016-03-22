from sat import *
import sys
from read_file import *

input_file = readDimacs(sys.argv[1])

print("Reading *.cnf file")
print("Finding solution")
sol=solve(input_file,[])
bs = buildSoultion(sol)
h=input_file.evaluate(bs)
print "Solution: ",bs
print "Evaluation of solution:", h