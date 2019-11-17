# -*- coding: utf-8 -*-

# input
N = int(input())
S = input()

# solve
ans = False
if S[0:int(N/2)] == S[int(N/2):]:
    ans = True

# output
print('Yes' if ans else 'No')
