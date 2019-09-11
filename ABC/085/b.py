# -*- coding: utf-8 -*-

# input
N = int(input())
d = list()
for _ in range(N):
    d.append(int(input()))

# solve & output
print(len(list(set(d))))
