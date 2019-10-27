# -*- coding: utf-8 -*-

# input
N = int(input())
D, X = map(int, input().split())
A = list()
for i in range(N):
    A.append(int(input()))

# solve
ans = [0] * D
for i in range(N):
    d = 1
    c = 1
    while d <= D:
        ans[d - 1] += 1
        d = c * A[i] + 1
        c += 1

# output
print(sum(ans) + X)
