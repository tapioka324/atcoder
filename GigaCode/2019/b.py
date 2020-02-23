# -*- coding: utf-8 -*-

N, X, Y, Z = map(int, input().split())
A = list()
B = list()
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 0
for a, b in zip(A, B):
    if a >= X and b >= Y and a + b >= Z:
        ans += 1

print(ans)
