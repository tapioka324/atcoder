# -*- coding: utf-8 -*-

# input
N = int(input())
A = list(map(int, input().split()))

# solve
ans = 0
for i in range(N):
    ans += 1 / A[i]

# output
print(1 / ans)
