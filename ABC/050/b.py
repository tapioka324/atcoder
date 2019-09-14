# -*- coding: utf-8 -*-

# input
N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for i in range(M)]

# solve & output
ans = sum(T)
for i in range(M):
    diff = PX[i][1] - T[PX[i][0] - 1]
    print(ans + diff)
