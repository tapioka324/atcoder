# -*- coding: utf-8 -*-

N = int(input())
H = list(map(int, input().split()))

ans = True
tmp = 0
for i in range(N):
    if H[i] - 1 >= tmp:
        H[i] -= 1
    if H[i] < tmp:
        ans = False
        break
    tmp = H[i]

print('Yes' if ans else 'No')
