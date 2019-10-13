# -*- coding: utf-8 -*-

# input
A, D = map(int, input().split())

# solve & output
print(max((A + 1) * D, (D + 1) * A))
