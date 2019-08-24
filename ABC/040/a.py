# -*- coding: utf-8 -*-

# input
n, x = map(int, input().split())

# solve & output
print(min(x - 1, n - x))
