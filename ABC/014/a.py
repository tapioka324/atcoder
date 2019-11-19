# -*- coding: utf-8 -*-

# input
a = int(input())
b = int(input())

# solve & output
print(b - a % b if a % b != 0 else '0')
