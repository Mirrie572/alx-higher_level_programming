#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for key, val in sorted(list(a_dictionary.items())):
        print("{:s}: {}".format(key, val))
