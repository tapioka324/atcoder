# -*- coding: utf-8 -*-

# input
N, Q = map(int, input().split())
L = [0] * Q
R = [0] * Q
T = [0] * Q
for i in range(Q):
    L[i], R[i], T[i] = map(int, input().split())

# solve
ans = [0] * N
for i in range(Q):
    for j in range(L[i] - 1, R[i]):
        ans[j] = T[i]

# output
for i in range(N):
    print(ans[i])
