# -*- coding: utf-8 -*-

# input
N = int(input())
d = list(map(int, input().split()))

# solve
ans = 0
d = sorted(d)
center = int(N / 2)
if d[center - 1] != d[center]:
    for i in range(d[center] - d[center - 1]):
        ans += 1

# output
print(ans)
