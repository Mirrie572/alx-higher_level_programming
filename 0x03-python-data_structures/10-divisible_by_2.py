#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        results = []
        for element in my_list:
            if element % 2 == 0:
                results.append(True)
            else:
                results.append(False)
        return results
