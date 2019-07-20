# -*- coding: utf-8 -*-
import math

# input
N, D = map(int, input().split())

# solve & output
print(math.ceil(N / (2 * D + 1)))
