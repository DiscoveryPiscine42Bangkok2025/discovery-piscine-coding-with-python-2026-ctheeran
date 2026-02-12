#!/usr/bin/env python

dupont_family = {
    "florian" : "red",
    "marie" : "blond",
    "virginie" : "brunette",
    "david" : "red",
    "franck" : "red"
}

def find_the_redheads(dict):
    redheads = [name for name, color in (filter(lambda x: x[1] == "red", dict.items()))]
    return redheads

print(find_the_redheads(dupont_family))
