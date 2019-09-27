# -*- coding: utf-8 -*-

# input
A, B, C = map(int, input().split())

# solve & output
if A + B == C and A - B == C:
    print('?')
elif A + B == C and A - B != C:
    print('+')
elif A + B != C and A - B == C:
    print('-')
else:
    print('!')
