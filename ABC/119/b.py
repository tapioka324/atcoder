# -*- coding: utf-8 -*-

# input
N = int(input())

# solve
ans = 0
for i in range(N):
    x, u = map(str, input().split())
    if u == 'JPY':
        ans += int(x)
    if u == 'BTC':
        ans += 380000.0 * float(x)

# output
print(ans)
