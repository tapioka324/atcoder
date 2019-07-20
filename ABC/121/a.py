# -*- coding: utf-8 -*-

# input
H, W = map(int, input().split())
A, B = map(int, input().split())

# solve
ans = (H * W) - (A * W + B * H - A * B)

# output
print(ans)
