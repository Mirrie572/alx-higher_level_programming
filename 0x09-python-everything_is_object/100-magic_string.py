#!/usr/bin/python3
def magic_string():
    magic_string.time_invoked = getattr(magic_string, 'time_invoked', 0) + 1
    return "BestSchool" + ", BestSchool" * (magic_string.time_invoked - 1)
