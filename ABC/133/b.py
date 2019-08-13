# -*- coding: utf-8 -*-
import math

# input
N, D = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]

# solve
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        dis = 0
        for k in range(D):
            dis += abs(X[i][k] - X[j][k])**2
        if math.sqrt(dis).is_integer():
            ans += 1

# output
print(ans)
