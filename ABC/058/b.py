# -*- coding: utf-8 -*-

# input
O = list(input())
E = list(input())

# solve & output
for i in range(len(O) + len(E)):
    if i % 2 == 0:
        print(O.pop(0), end='')
    else:
        print(E.pop(0), end='')
