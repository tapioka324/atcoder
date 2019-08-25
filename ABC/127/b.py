# -*- coding: utf-8 -*-

# input
r, D, x = map(int, input().split())

# solve & output
tmp = x
for i in range(10):
    ans = r * tmp - D
    print(ans)
    tmp = ans
