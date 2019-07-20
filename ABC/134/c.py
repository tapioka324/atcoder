# -*- coding: utf-8 -*-
import copy

# input
N = int(input())
A = list()
for _ in range(N):
    A.append(int(input()))

# solve & output
ans = copy.copy(A)
ans.sort()
m = ans[-1]
for i in range(N):
    if A[i] != m:
        print(m)
    else:
        print(ans[N - 2])
