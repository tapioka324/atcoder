# -*- coding: utf-8 -*-

# input
X, t = map(int, input().split())

# solve & output
print(X - t if X > t else 0)
