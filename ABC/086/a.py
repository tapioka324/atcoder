# -*- coding: utf-8 -*-

# input
a, b = map(int, input().split())

# solve & output
print('Even' if (a * b) % 2 == 0 else 'Odd')
