# -*- coding: utf-8 -*-

# input
N = int(input())

# solve
ans = int(N / 111)
if N % 111 != 0:
    ans += 1

# output
print(ans * 111)
