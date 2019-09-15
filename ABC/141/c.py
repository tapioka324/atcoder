# -*- coding: utf-8 -*-

# input
N, K, Q = map(int, input().split())
A = list()
for _ in range(Q):
    A.append(int(input()))

# solve
ans = [K - Q] * N
for i in range(Q):
    ans[A[i] - 1] += 1

# output
for i in range(N):
    if ans[i] <= 0:
        print('No')
    else:
        print('Yes')
