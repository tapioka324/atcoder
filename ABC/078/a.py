# -*- coding: utf-8 -*-

# input
X, Y = input().split()

# solve
l = ['A', 'B', 'C', 'D', 'E', 'F']

if l.index(X) < l.index(Y):
    ans = '<'
elif l.index(X) > l.index(Y):
    ans = '>'
else:
    ans = '='

# output
print(ans)
