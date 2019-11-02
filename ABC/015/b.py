# -*- coding: utf-8 -*-
import math

# input
N = int(input())
A = list(map(int, input().split()))

# solve
count = 0
for i in range(N):
    if A[i] != 0: count += 1

# output
print(math.ceil(sum(A) / count))
