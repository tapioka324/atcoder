# -*- coding: utf-8 -*-
import math

# input
N = int(input())
R = list()
for i in range(N):
    R.append(int(input()))

# solve
R.sort(reverse=True)
ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += R[i] ** 2
    else:
        ans -= R[i] ** 2

# output
print(ans * math.pi)
