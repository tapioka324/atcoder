# -*- coding: utf-8 -*-

# input
A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

# solve & output
print((A - C) * S + (B - C) * T if S + T >= K else A * S + B * T)
