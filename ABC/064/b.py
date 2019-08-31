# -*- coding: utf-8 -*-

# input
N = int(input())
a = list(map(int, input().split()))

# solve
a.sort()

# output
print(a[-1] - a[0])
