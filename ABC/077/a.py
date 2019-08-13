# -*- coding: utf-8 -*-

# input
C1 = list(input())
C2 = list(input())

# solve & output
print('YES' if C1 == C2[::-1] and C2 == C1[::-1] else 'NO')
