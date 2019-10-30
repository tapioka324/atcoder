# -*- coding: utf-8 -*-

# input
a, b = map(int, input().split())

# solve & output
print(a if a <= b else a - 1)
