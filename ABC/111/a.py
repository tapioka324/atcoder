# -*- coding: utf-8 -*-

# input
n = input()

# solve & output
print(n.translate(str.maketrans({'1': '9', '9': '1'})))
