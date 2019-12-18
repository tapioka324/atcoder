# -*- coding: utf-8 -*-

N = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == 2025 - N:
            print('{} x {}'.format(i, j))
