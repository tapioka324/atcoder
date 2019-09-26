# -*- coding: utf-8 -*-

# input
N, T = map(int, input().split())
c = [0] * N
t = [0] * N
for i in range(N):
    _c, _t = map(int, input().split())
    c[i] = _c
    t[i] = _t

# solve
ans = 1001
for i in range(N):
    if t[i] <= T:
        ans = min(ans, c[i])

# output
print(ans if ans != 1001 else 'TLE')
