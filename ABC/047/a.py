# -*- coding: utf-8 -*-

# input
l = list(map(int, input().split()))

# solve
l.sort()

# output
print('Yes' if sum(l[0:2]) == l[-1] else 'No')
