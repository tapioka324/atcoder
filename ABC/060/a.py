# -*- coding: utf-8 -*-

# input
A, B, C = map(str, input().split())

# solve & output
print('YES' if A[-1] == B[0] and B[-1] == C[0] else 'NO')
