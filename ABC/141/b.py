# -*- coding: utf-8 -*-

# input
S = input()

# solve
ans = True
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == 'L':
            ans = False
            break
    else:
        if S[i] == 'R':
            ans = False
            break

# output
print('Yes' if ans else 'No')
