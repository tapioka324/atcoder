# -*- coding: utf-8 -*-

# input
A, B, C = map(int, input().split())

# solve & output
print(C - (A - B) if (A - B) < C else 0)
