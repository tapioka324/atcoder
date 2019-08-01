# -*- coding: utf-8 -*-

# input
A, B, C, D = map(int, input().split())

# solve
if (A + B) > (C + D):
    ans = 'Left'
elif (A + B) < (C + D):
    ans = 'Right'
else:
    ans = 'Balanced'

# output
print(ans)
