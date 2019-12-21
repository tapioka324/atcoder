# -*- coding: utf-8 -*-

A = list(map(int, input().split()))

print('bust' if sum(A) >= 22 else 'win')
