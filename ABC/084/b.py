# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())
S = input()

# solve
ans = True
for i in range(A + B + 1):
    if i == A:
        if S[A] != '-':
            ans = False
            break
    else:
        if not S[i].isdigit():
            ans = False
            break

# output
print('Yes' if ans else 'No')
