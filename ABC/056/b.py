# -*- coding: utf-8 -*-

# input
W, a, b = map(int, input().split())

# solve
if a <= b:
    if b <= a+W:
        ans = 0
    else:
        ans = b - (a+W)
else:
    ans = a - (b+W)

# output
print(ans)
