# -*- coding: utf-8 -*-

# input
x, a, b = map(int, input().split())

# solve
ans = 'A' if abs(x - a) < abs(x - b) else 'B'

# output
print(ans)
