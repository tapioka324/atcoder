# -*- coding: utf-8 -*-

# input
N = int(input())
d = list(map(int, input().split()))

# solve
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        ans += d[i] * d[j]

# output
print(ans)
