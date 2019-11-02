# -*- coding: utf-8 -*-

# input
N = int(input())

# solve
ans = False
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == N:
            ans = True
            break

# output
print('Yes' if ans else 'No')
