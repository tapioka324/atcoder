# -*- coding: utf-8 -*-

# input
A, B, C = map(int, input().split())

# solve
ans = (A * B * C) % (10**9 + 7)

# output
print(ans)
