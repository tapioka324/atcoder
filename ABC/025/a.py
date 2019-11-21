# -*- coding: utf-8 -*-

# input
S = sorted(list(input()))
N = int(input())

# solve & output
print(S[int((N - 1)/ 5)] + S[(N - 1) % 5])
