# -*- coding: utf-8 -*-

# input
D = int(input())

# solve
ans = 'Christmas'
if D == 24:
    ans += ' Eve'
if D == 23:
    ans += ' Eve Eve'
if D == 22:
    ans += ' Eve Eve Eve'

# output
print(ans)
