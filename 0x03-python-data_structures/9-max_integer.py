#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    if my_list:
        max_int = my_list.copy()
        max_int.sort()
        return max_int[-1]
