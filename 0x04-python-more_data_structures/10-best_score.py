#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    a = list(a_dictionary.values())
    a = list(a_dictionary.keys())
    return b[a.index(max(a))]
