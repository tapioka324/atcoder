# -*- coding: utf-8 -*-

# input
R = int(input())

# solve
if R < 1200:
    ans = 'ABC'
elif R < 2800:
    ans = 'ARC'
else:
    ans = 'AGC'

# output
print(ans)
