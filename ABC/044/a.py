# -*- coding: utf-8 -*-

# input
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

# solve & output
print(X * K + Y * (N - K) if N >= K else X * N)
