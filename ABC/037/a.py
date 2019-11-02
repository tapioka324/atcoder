# -*- coding: utf-8 -*-

# input
A, B, C = map(int, input().split())

# solve
ans = 0
while C > 0:
    C -= min(A, B)
    if C >= 0: ans += 1

# output
print(ans)
