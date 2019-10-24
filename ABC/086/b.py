# -*- coding: utf-8 -*-

# input
a, b = input().split()

# solve
ans = False
for i in range(1, 1000):
    if i * i == int(a + b):
        ans = True

# output
print('Yes' if ans else 'No')
