# -*- coding: utf-8 -*-

N = int(input())
K = int(input())
X = list(map(int, input().split()))

ans = 0
for x in X:
    ans += min(x * 2, (K - x) * 2)

print(ans)
