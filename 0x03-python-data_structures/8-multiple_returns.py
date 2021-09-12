#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = (len(sentence), sentence[0] if len(sentence) > 0 else None)
    return first_char
