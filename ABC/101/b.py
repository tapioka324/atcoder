# -*- coding: utf-8 -*-

# input
N = input()

# solve
S = 0
for i in range(len(N)):
    S += int(N[i])

# output
print('Yes' if int(N) % S == 0 else 'No')
