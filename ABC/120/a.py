# -*- coding: utf-8 -*-

# input
A, B, C = map(int, input().split())

# solve & output
print(C if int(B / A) >= C else int(B / A))
