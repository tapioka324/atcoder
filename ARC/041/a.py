# -*- coding: utf-8 -*-

x, y = map(int, input().split())
k = int(input())

print(min(y, k) + x - (k - min(y, k)))
