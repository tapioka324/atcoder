# -*- coding: utf-8 -*-

# input
a, b, c = map(int, input().split())

# solve & output
print(min(a + b, a + c, b + c))
