# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())

# solve & output
print(max(A + B, A - B, A * B))
