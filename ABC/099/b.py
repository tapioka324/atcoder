# -*- coding: utf-8 -*-

# input
a, b = map(int, input().split())

# solve
n = b - a
ans = n * (n + 1) / 2 - b

# output
print(int(ans))
