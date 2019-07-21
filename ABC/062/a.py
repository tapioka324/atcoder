# -*- coding: utf-8 -*-

# input
x, y = map(int, input().split())

# solve
ans = [0, 1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]

# output
print('Yes' if ans[x] == ans[y] else 'No')
