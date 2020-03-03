# -*- coding: utf-8 -*-

N = int(input())
S = list()
for i in range(N):
    s = input()
    S.append(s)

r = 0
b = 0
for s in S:
    r += s.count('R')
    b += s.count('B')

if r > b:
    print('TAKAHASHI')
elif r < b:
    print('AOKI')
else:
    print('DRAW')
