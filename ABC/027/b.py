# -*- coding: utf-8 -*-

N = int(input())
a = list(map(int, input().split()))

if sum(a) % N == 0:
    ans = 0
    ave = sum(a) // N
    tmp = 0
    for i in range(N):
        tmp += (a[i] - ave)
        if tmp != 0:
            ans += 1
    print(ans)
else:
    print('-1')
