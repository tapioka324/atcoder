# -*- coding: utf-8 -*-

# input
ans = list(map(int, input().split()))

# solve
ans.sort()

# output
print('YES' if ans == [5, 5, 7] else 'NO')
