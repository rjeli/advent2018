#!/usr/bin/env python
import sys

freq = 0

with open('input.txt', 'r') as f:
    ls = f.readlines()
    ns = [int(l) for l in ls]

seen = set()
i = 0
while True:
    for n in ns:
        if freq in seen:
            print freq
            sys.exit()
        seen.add(freq)
        freq += n
