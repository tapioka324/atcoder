# -*- coding: utf-8 -*-

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
num = len(list(set(A)))
c = [0] * A[-1]
for a in A:
    c[a - 1] += 1
c.sort()
ans = 0
if num > K:
    i = 0
    diff = 0
    while diff != num - K:
        if c[i] != 0:
            ans += c[i]
            i += 1
            diff += 1
        else:
            i += 1

print(ans)
