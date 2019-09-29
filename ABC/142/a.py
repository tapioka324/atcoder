# -*- coding: utf-8 -*-

# input
N = int(input())

# solve
odd = 0
for i in range(1, N + 1):
    if i % 2 == 1:
        odd += 1

# output
print(odd / N)
