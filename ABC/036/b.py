# -*- coding: utf-8 -*-

N = int(input())
s = [list(input()) for i in range(N)]

for i in range(N):
    for j in reversed(range(N)):
        print(s[j][i], sep='', end='')
    print()
