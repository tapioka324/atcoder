# -*- coding: utf-8 -*-

S, T = map(str, input().split())
A, B = map(int, input().split())
U = input()

print('{} {}'.format(A - 1, B) if U == S else '{} {}'.format(A, B - 1))
