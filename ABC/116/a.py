# -*- coding: utf-8 -*-

# input
l = list(map(int, input().split()))

# solve
l.sort()
ans = int(l[0] * l[1] / 2)

# output
print(ans)
