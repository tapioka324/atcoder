# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())

# solve & output
print(A * B if A <= 9 and B <= 9 else '-1')
