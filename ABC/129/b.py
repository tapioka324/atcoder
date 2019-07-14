# -*- coding: utf-8 -*-

# input
N = int(input())
W = list(map(int, input().split()))

# solve
ans = sum(W)
for i in range(1, len(W)):
    ans = min(ans, abs(sum(W[0:i]) - sum(W[i::])))

# output
print(ans)
