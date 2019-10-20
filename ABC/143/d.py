# -*- coding: utf-8 -*-
import bisect

# input
N = int(input())
L = list(map(int, input().split()))

# solve
ans = 0
L.sort()
for i in range(N):
    for j in range(i + 1, N):
        r = bisect.bisect_left(L, L[i] + L[j])
        l = j + 1
        ans += max(0, r - l)

# output
print(ans)
