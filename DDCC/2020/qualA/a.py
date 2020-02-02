# -*- coding: utf-8 -*-

X, Y = map(int, input().split())

ans = 0
ans += max(0, (4 - X) * 100000)
ans += max(0, (4 - Y) * 100000)
if X == 1 and Y == 1:
    ans += 400000

print(ans)
