# -*- coding: utf-8 -*-

import math

N = int(input())
X = list()
Y = list()
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        ans = max(ans, math.sqrt(pow(X[i] - X[j], 2) + pow(Y[i] - Y[j], 2)))

print(ans)
