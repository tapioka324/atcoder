# -*- coding: utf-8 -*-

N = int(input())
SP = list()
for i in range(N):
    s, p = map(str, input().split())
    SP.append([s, int(p), i + 1])

SP.sort(key=lambda x: x[1], reverse=True)
SP.sort(key=lambda x: x[0])

for sp in SP:
    print(sp[2])
