# -*- coding: utf-8 -*-

N = int(input())

ans = 1
count = 0
for i in range(1, N + 1):
    c = 0
    tmp = i
    if tmp % 2 == 0:
        c += 1
        tmp /= 2
        while tmp % 2 == 0:
            c += 1
            tmp /= 2
    if count < c:
        ans = i
        count = c

print(ans)
