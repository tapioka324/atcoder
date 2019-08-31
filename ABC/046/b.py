# -*- coding: utf-8 -*-

# input
N, K = map(int, input().split())

# solve & output
print(K * ((K-1) ** (N-1)))
