# -*- coding: utf-8 -*-

# input
N = int(input())
L = list(map(int, input().split()))

# solve
L.sort()
ans = 'Yes' if L[-1] < sum(L[:-1]) else 'No'

# output
print(ans)
