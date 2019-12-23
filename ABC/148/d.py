# -*- coding: utf-8 -*-

N = int(input())
a = list(map(int, input().split()))

ans = 0
pos = 1
for i in range(N):
    if a[i] != pos:
        ans += 1
    else:
        pos += 1

print(ans if ans < N else -1)
