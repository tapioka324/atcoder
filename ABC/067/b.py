# -*- coding: utf-8 -*-

# input
N, K = map(int, input().split())
l = list(map(int, input().split()))

# solve
l.sort(reverse=True)

# output
print(sum(l[0:K]))
