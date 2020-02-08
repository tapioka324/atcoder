# -*- coding: utf-8 -*-

s = input()

ans = True
for i, j in zip(s, reversed(s)):
    if i != j and i != '*' and j != '*':
        ans = False
        break

print('YES' if ans else 'NO')
