# -*- coding: utf-8 -*-

N, M = map(int, input().split())

if N * 2 <= M:
    ans = N + (M - N * 2) // 4
else:
    ans = M // 2

print(ans)
