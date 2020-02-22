# -*- coding: utf-8 -*-

N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
m = max(A)
for i in range(N):
    A[i] -= m
    A[i] += X
    if A[i] >= 0:
        ans += 1

print(ans)
