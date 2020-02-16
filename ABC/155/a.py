# -*- coding: utf-8 -*-

A, B, C = map(int, input().split())

print('Yes' if len(set([A, B, C])) == 2 else 'No')
