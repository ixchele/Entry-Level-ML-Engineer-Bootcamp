#!/usr/bin/env python3
from sys import argv

rng = reversed(range(1, len(argv)));
for j in rng:
    print(argv[j][::-1].swapcase(), end=' ' if j > 1 else '\n')

