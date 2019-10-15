# -*- coding: utf-8 -*-

# input
A, B, C, D, E = map(int, input().split())

# solve & output
print(max(A + D + E, B + C + E))
