# -*- coding: utf-8 -*-

# input
N, M, X = map(int, input().split())
A = list(map(int, input().split()))

# solve
cost = [0] * (N + 1)
for i in range(M):
    cost[A[i]] = 1

# output
print(min(sum(cost[:X]), sum(cost[X + 1:])))
