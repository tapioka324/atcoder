# -*- coding: utf-8 -*-

# input
N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

# solve
ans = 0
min_ave_temp = T - H[0] * 0.006
for i in range(1, N):
    ave_temp = T - H[i] * 0.006
    if abs(A - ave_temp) < abs(A - min_ave_temp):
        ans = i
        min_ave_temp = ave_temp

# output
print(ans + 1)
