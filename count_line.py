from __future__ import print_function
from __future__ import division
try:
    import json
except ImportError:
    import simplejson as json
import string
import sys

def main():
    filename = sys.argv[1]
    inFile = open("%s" %(filename), "r")
    count  = 0
    for line in inFile:
        count += 1
        
    print(count)
 # ---------------------- #
if __name__ == "__main__":
    main()
