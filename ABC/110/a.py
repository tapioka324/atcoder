# -*- coding: utf-8 -*-

# input
l = list(map(int, input().split()))

# solve
l.sort()

# output
print(l[-1] * 10 + l[1] + l[0])
