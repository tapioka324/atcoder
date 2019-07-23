# -*- coding: utf-8 -*-

# input
N, K = map(int, input().split())

# solve & output
print(0 if N % K == 0 else 1)
