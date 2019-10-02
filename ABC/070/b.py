# -*- coding: utf-8 -*-

# input
A, B, C, D = map(int, input().split())

# solve & output
print(max(0, min(B, D) - max(A, C)))
