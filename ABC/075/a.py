# -*- coding: utf-8 -*-

# input
A, B, C = map(int, input().split())

# solve
if A == B:
    ans = C
elif B == C:
    ans = A
else:
    ans = B

# output
print(ans)
