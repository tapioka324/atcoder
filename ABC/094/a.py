# -*- coding: utf-8 -*-

# input
A, B, X = map(int, input().split())

# solve
ans = 'YES' if A <= X and (X - A) <= B else 'NO'

# output
print(ans)
