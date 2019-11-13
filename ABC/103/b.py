# -*- coding: utf-8 -*-

# input
S = input()
T = input()

# solve
ans = False
for i in range(len(S)):
    S = S[len(S) - 1] + S[0:len(S) - 1]
    if S == T:
        ans = True
        break

# output
print('Yes' if ans else 'No')
