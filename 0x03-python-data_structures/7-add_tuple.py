#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sequence = [0, 0]
    if len(tuple_a) >= 1:
        sequence[0] += tuple_a[0]
    if len(tuple_a) >= 2:
        sequence[1] += tuple_a[1]
    if len(tuple_b) >= 1:
        sequence[0] += tuple_b[0]
    if len(tuple_b) >= 2:
        sequence[1] += tuple_b[1]
    tupled = (sequence[0], sequence[1])
    return tupled
