# -*- coding: utf-8 -*-

# input
S = input()

# solve & output
for i in range(6):
    if i < 5:
        print(S.count(chr(ord('A') + i)), end=' ')
    else:
        print(S.count(chr(ord('A') + i)))
