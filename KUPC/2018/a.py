# -*- coding: utf-8 -*-

N = int(input())
S = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
for s, a in zip(S, A):
    ans = max(ans, s * a)

print(ans)
