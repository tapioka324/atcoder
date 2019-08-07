# -*- coding: utf-8 -*-

# input
N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

# solve
ans = 0
for i in range(N):
    diff = V[i] - C[i]
    if diff > 0:
        ans += diff

# output
print(ans)
