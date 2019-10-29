# -*- coding: utf-8 -*-

# input
A, B, C = map(int, input().split())
K = int(input())

# solve & output
print(A + B + C + (max(A, B, C) * ((1 << K) - 1)))
