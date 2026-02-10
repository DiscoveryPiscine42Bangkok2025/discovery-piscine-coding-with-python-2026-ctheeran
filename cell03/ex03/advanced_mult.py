#!/usr/bin/env python

i= 0

while i != 11:
    k = 0
    print(f"Table of {i} = ", end="")
    
    while k != 11:
            print(i*k, end=" ")
            k += 1
    
    print()
    i += 1
