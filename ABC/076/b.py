# -*- coding: utf-8 -*-

# input
N = int(input())
K = int(input())

# solve
ans = 1
for i in range(N):
    ans = min(2*ans, ans+K)

# output
print(ans)
