# -*- coding: utf-8 -*-

# input
S = input()

# solve
ans = False
if S[0] == 'A' and S[1] != 'C' and S[2:len(S) - 1].count('C') == 1 and S.replace('A', '').replace('C', '').islower():
    ans = True

# output
print('AC' if ans else 'WA')
