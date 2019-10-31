# -*- coding: utf-8 -*-

# input
N = int(input())

# solve
i = 1
while i * i <= N:
    i += 1

# output
print((i - 1) ** 2)
