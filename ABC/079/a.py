# -*- coding: utf-8 -*-

# input
N = input()

# solve
ans = False
if (N[0] == N[1] and N[1]== N[2]) or (N[1] == N[2] and N[2]== N[3]):
    ans = True

# output
print('Yes' if ans else 'No')
