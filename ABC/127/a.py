# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())

# solve
if A >= 13:
    ans = B
elif 6 <= A <= 12:
    ans = int(B / 2)
else:
    ans = 0

# output
print(ans)
