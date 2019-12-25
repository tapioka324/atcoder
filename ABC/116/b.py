# -*- coding: utf-8 -*-

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())

if s == 1 or s == 2:
    print(4)
    exit()
ans = 2
while s > 1:
    s = f(s)
    ans += 1

print(ans)
