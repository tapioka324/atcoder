# -*- coding: utf-8 -*-

# input
N, K = map(int, input().split())
h = list(map(int, input().split()))

# solve
ans = 0
for i in range(N):
    if h[i] >= K:
        ans += 1

# output
print(ans)
