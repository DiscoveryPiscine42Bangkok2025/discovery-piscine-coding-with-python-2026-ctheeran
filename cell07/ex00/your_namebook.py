#!/usr/bin/env python

persons = {
    "jean" : "valjean",
    "grace" : "hopper",
    "xavier" : "niel",
    "fifi" : "brindacier"
}

def array_of_names(dict):
    full_name = []
    for key, value in dict.items():
        fullname = key.capitalize() + " " + value.capitalize()
        full_name.append(fullname)
    return(full_name)

print(array_of_names(persons))
