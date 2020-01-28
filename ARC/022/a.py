# -*- coding: utf-8 -*-

S = input()

p = 0
for s in S:
    if (s == 'i' or s == 'I') and p == 0:
        p = 1
    if (s == 'c' or s == 'C') and p == 1:
        p = 2
    if (s == 't' or s == 'T') and p == 2:
        p = 3
        break

print('YES' if p == 3 else 'NO')
