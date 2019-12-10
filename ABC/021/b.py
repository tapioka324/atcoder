# -*- coding: utf-8 -*-

N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

ans = True
for p in P:
    if p == a or p == b or P.count(p) >= 2:
        ans = False
        break

print('YES' if ans else 'NO')
