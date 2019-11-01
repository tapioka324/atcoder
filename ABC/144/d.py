# -*- coding: utf-8 -*-
import math

# input
a, b, x = map(int, input().split())

# solve
S = x / a
if (S >= (a * b) / 2):
    h = (a * b - S) * 2 / a
    rad = math.atan2(h, a)
else:
    w = S * 2 / b
    rad = math.atan2(b, w)

# output
print(rad / (2 * math.pi) * 360)
