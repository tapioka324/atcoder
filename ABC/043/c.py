# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))

ave = round(sum(A) / N)
ans = 0
for a in A:
    ans += (a - ave) ** 2

print(ans)
