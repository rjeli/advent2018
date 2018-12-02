#!/usr/bin/env python
from collections import Counter

with open('input.txt', 'r') as f:
    ls = [l.strip() for l in f.readlines()]

twos = 0
threes = 0

for l in ls:
    c = Counter()
    for ch in l:
        c[ch] += 1
    got_two, got_three = False, False
    for ch, cnt in c.items():
        if cnt == 2:
            got_two = True
        elif cnt == 3:
            got_three = True
    if got_two:
        twos += 1
    if got_three:
        threes += 1
        
print twos
print threes
print twos * threes
