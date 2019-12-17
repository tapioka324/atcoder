# -*- coding: utf-8 -*-

import math

xa, ya, xb, yb, T, V = map(int, input().split())
n = int(input())
X = list()
Y = list()
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = False
for x, y in zip(X, Y):
    l = math.sqrt((x - xa) ** 2 + (y - ya) ** 2) + math.sqrt((xb - x) ** 2 + (yb - y) ** 2)
    if l <= V * T:
        ans = True
        break

print('YES' if ans else 'NO')
