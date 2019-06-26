# -*- coding: utf-8 -*-

# input
P, Q, R = map(int, input().split())

# solve & output
print((P + Q + R) - max(P, Q, R))
