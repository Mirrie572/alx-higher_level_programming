#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        biggest = sorted(list(a_dictionary.values()))[-1]
        for key, value in a_dictionary.items():
            if value == biggest:
                return key
    else:
        return None
