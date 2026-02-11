#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
    parameter = input("What was the parameter? : ")
    if parameter == "Hello":
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("None")
