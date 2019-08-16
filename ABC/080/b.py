# -*- coding: utf-8 -*-

# input
N = input()

# solve
f = 0
for i in range(len(N)):
    f += int(N[i])

# output
print('Yes' if int(N) % f == 0 else 'No')
