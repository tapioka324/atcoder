# -*- coding: utf-8 -*-

# input
A = int(input())
B = int(input())

# solve
if A > B:
    ans = 'GREATER'
elif A < B:
    ans = 'LESS'
else:
    ans = 'EQUAL'

# output
print(ans)
