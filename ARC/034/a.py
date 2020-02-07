# -*- coding: utf-8 -*-

N = int(input())
l = list()
for _ in range(N):
    l.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    ans = max(ans, sum(l[i][0:4]) + l[i][4] * 110 / 900)

print(ans)
