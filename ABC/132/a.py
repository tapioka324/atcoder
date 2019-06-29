# -*- coding: utf-8 -*-

# input
S = list(input())

# solve
S = sorted(S)
ans = 'Yes' if S[0] == S[1] and S[1] != S[2] and S[2] == S[3]else 'No'

# output
print(ans)
