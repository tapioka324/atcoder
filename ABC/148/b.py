# -*- coding: utf-8 -*-

N = int(input())
S, T = map(str, input().split())

for s, t in zip(S, T):
    print(s, t, sep='', end='')
