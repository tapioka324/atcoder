# -*- coding: utf-8 -*-

# input
N = int(input())

# solve
l = [0] * (N + 1)
l[0] = 2
l[1] = 1
for i in range(2, N + 1):
    l[i] = l[i - 1] + l[i - 2]

# output
print(l[-1])
