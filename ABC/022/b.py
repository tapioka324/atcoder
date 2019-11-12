# -*- coding: utf-8 -*-

# input
N = int(input())
A = list()
for i in range(N):
    A.append(int(input()))

# solve & output
print(len(A) - len(set(A)))
