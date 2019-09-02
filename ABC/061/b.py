# -*- coding: utf-8 -*-

# input
N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(M)]

# solve
ans = [0] * N
for i in range(M):
    ans[ab[i][0] - 1] += 1
    ans[ab[i][1] - 1] += 1

# output
for i in range(N):
    print(ans[i])
