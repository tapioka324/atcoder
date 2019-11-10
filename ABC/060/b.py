# -*- coding: utf-8 -*-

# input
A, B, C = map(int, input().split())

# solve
ans = False
for i in range(B):
    if (A * i) % B == C:
        ans = True
        break

# output
print('YES' if ans else 'NO')
