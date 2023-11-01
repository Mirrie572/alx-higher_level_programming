#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    c = 0
    space = ""
    for char in str:
        if c == n:
            c += 1
            continue
        space += str[c]
        c += 1
    return space
