# -*- coding: utf-8 -*-

# input
N = int(input())
A = list(map(int, input().split()))

# solve
A.sort()

# output
print(A[-1] - A[0])
