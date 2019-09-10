# -*- coding: utf-8 -*-

# input
N = int(input())
a = list(map(int, input().split()))

# solve
a.sort(reverse=True)

# output
print(sum(a[::2]) - sum(a[1::2]))
