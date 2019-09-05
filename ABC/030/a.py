# -*- coding: utf-8 -*-

# input
A, B, C, D = map(int, input().split())

# solve
if B / A > D / C:
    ans = 'TAKAHASHI'
elif B/ A < D / C:
    ans = 'AOKI'
else:
    ans = 'DRAW'

# output
print(ans)
