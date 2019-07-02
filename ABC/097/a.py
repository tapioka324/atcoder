# -*- coding: utf-8 -*-

# input
a, b, c, d = map(int, input().split())

# solve
ans = 'Yes' if (abs(a - b) <= d and abs(b - c) <= d) or abs(a - c) <= d else 'No'

# output
print(ans)
