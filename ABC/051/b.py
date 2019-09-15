# -*- coding: utf-8 -*-

# input
K, S = map(int, input().split())

# solve
ans = 0
for X in range(K + 1):
    for Y in range(K + 1):
        Z = S - X - Y
        if 0 <= Z and Z <= K:
            ans += 1

# output
print(ans)
