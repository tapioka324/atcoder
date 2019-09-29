# -*- coding: utf-8 -*-

# input
N = int(input())
A = list(map(int, input().split()))

# solve
ans = [0] * N
for i in range(N):
    ans[A[i] - 1] = i + 1

# output
for i in range(N):
    print(ans[i], end=' ')
