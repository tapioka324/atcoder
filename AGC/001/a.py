# -*- coding: utf-8 -*-

N = int(input())
L = sorted(list(map(int, input().split())))

ans = 0
for i in range(N):
    ans += min(L[2 * i], L[2 * i + 1])

print(ans)
