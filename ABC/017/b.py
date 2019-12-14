# -*- coding: utf-8 -*-

X = input()

for i in ('ch', 'o', 'k', 'u'):
    X = X.replace(i, '')

print('YES' if not X else 'NO')
