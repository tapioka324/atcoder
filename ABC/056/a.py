# -*- coding: utf-8 -*-

# input
a, b = input().split()

# solve
if a == 'H':
    ans = b
else:
    if b == 'H':
        ans = 'D'
    else:
        ans = 'H'

# output
print(ans)
