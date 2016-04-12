from sat import *
import sys
from read_file import *

input_file = readDimacs(sys.argv[1])
sol = solve(input_file,[])
if sol == False:
    print -1
else:
    for s in sol:
        if not isinstance(s,Not):
            print int(s.__str__()),
