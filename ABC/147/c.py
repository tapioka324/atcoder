# -*- coding: utf-8 -*-

N = int(input())
g = list([-1 for j in range(N)] for i in range(N))
for i in range(N):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        g[i][x - 1] = y

ans = 0
for i in range(1 << N):
    d = list((i >> j) & 1 for j in range(N))
    ok = True
    for j in range(N):
        if d[j]:
            for k in range(N):
                if g[j][k] == -1:
                    continue
                if g[j][k] != d[k]:
                    ok = False
    if ok:
        ans = max(ans, sum(d))

print(ans)
