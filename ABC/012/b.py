# -*- coding: utf-8 -*-

N = int(input())

h = N // 3600
N %= 3600
m = N // 60
N %= 60

print('{:02}:{:02}:{:02}'.format(h, m, N))
