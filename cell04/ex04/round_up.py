#!/usr/bin/env python
number = float(input("Give me a number : "))
number_int = int(number)
if (number - number_int > 0):
    print(f"{number_int + 1}")
