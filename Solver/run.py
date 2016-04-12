from sat import *
import sys
from read_file import *

input_file = readDimacs(sys.argv[1])
sol = solve(input_file,[])
if sol == False:
    print "Solution not found"
else:
    for s in sol:
        if not isinstance(s,Not):
            print int(s.__str__()),
        else:
            print -int(s.__str__()[1:]),
