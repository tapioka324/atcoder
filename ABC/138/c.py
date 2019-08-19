# -*- coding: utf-8 -*-

# input
N = int(input())
v = list(map(int, input().split()))

# solve
v.sort()
first = sum(v[0:2]) / 2
if N != 2:
    tmp = first
    for i in range(2, N):
        ans = (tmp + v[i]) / 2
        tmp = ans
else:
    ans = first

# output
print(ans)
