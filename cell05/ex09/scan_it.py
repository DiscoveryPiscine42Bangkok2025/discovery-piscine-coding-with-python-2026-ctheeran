#!/usr/bin/env python

import sys, re

if len(sys.argv) == 3:
    print(len(re.findall(sys.argv[1],sys.argv[2])))
else:
    print("None")
