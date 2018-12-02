#!/usr/bin/env python
from collections import Counter

with open('input.txt', 'r') as f:
    ls = [l.strip() for l in f.readlines()]

def remove_ch(s, idx):
    return s[:idx] + s[idx+1:]

assert remove_ch('asdf', 0) == 'sdf'
assert remove_ch('asdf', 1) == 'adf'
assert remove_ch('asdf', 3) == 'asd'

for l1 in ls:
    for l2 in ls:
        for i in xrange(len(l1)):
            if l1 != l2 and remove_ch(l1, i) == remove_ch(l2, i):
                print remove_ch(l1, i)
