# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())

# solve
ans = 'Yes' if (A * B) % 2 == 1 else 'No'

# output
print(ans)
