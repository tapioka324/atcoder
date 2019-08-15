# -*- coding: utf-8 -*-

# input
N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

# solve
ans = [0] * M
for i in range(N):
    for j in range(1, A[i][0] + 1):
        ans[A[i][j] - 1] += 1

# output
print(ans.count(N))
