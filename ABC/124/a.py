# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())

# solve & output
print(max(A + A - 1, B + B - 1, A + B))
