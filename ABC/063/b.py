# -*- coding: utf-8 -*-

# input
S = input()

# solve
is_diffrent = True
for i in range(len(S)):
    for j in range(i + 1, len(S)):
        if S[i] == S[j]:
            is_diffrent = False

# output
print('yes' if is_diffrent else 'no')
