# -*- coding: utf-8 -*-

# input
N = input()

# solve
ans = 'Yes' if N == N[::-1] else 'No'

# output
print(ans)
