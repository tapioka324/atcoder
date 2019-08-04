# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())

# solve & output
print(int((A + B) / 2) if (A + B) % 2 == 0 else 'IMPOSSIBLE')
