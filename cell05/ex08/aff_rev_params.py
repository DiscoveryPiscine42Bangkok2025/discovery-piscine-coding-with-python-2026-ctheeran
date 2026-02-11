#!/usr/bin/env python

import sys

sys_rev = [sys.argv[i] for i in range (len(sys.argv) - 1 , 0 , -1)]

if len(sys.argv) < 4:
    print("None")
else:
    for i in sys_rev:
        print(i)
