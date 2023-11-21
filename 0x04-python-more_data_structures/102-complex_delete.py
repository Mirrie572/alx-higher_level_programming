#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if value:
        for key, val in a_dictionary.copy().items():
            if a_dictionary[key] == value:
                del a_dictionary[key]
        return a_dictionary
