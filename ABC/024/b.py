# -*- coding: utf-8 -*-

N, T = map(int, input().split())
A = list(int(input()) for i in range(N))

ans = 0
closed = 0
for a in A:
    if closed <= a:
        ans += T
    else:
        ans += a - (closed - T)
    closed = a + T

print(ans)
