# -*- coding: utf-8 -*-

# input
A, B, C = map(int, input().split())

# solve & output
print('Yes' if A <= C and C <= B else 'No')
