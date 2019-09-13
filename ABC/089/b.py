# -*- coding: utf-8 -*-

# input
N = int(input())
S = list(map(str, input().split()))

# solve & output
print('Four' if S.count('Y') >= 1 else 'Three')
