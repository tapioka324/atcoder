# -*- coding: utf-8 -*-

N, K = map(int, input().split())
t = list()
for i in range(N):
    t.append(int(input()))

ans = -1
for i in range(2, N):
    if t[i - 2] + t[i - 1] + t[i] < K:
        ans = i + 1
        break

print(ans)
