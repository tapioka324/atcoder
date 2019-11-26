# -*- coding: utf-8 -*-

A, B, C, D = map(int, input())

if A + B + C + D == 7:
    print('{}+{}+{}+{}=7'.format(A, B, C, D))
elif A + B + C - D == 7:
    print('{}+{}+{}-{}=7'.format(A, B, C, D))
elif A + B - C + D == 7:
    print('{}+{}-{}+{}=7'.format(A, B, C, D))
elif A + B - C - D == 7:
    print('{}+{}-{}-{}=7'.format(A, B, C, D))
elif A - B + C + D == 7:
    print('{}-{}+{}+{}=7'.format(A, B, C, D))
elif A - B + C - D == 7:
    print('{}-{}+{}-{}=7'.format(A, B, C, D))
elif A - B - C + D == 7:
    print('{}-{}-{}+{}=7'.format(A, B, C, D))
elif A - B - C - D == 7:
    print('{}-{}-{}-{}=7'.format(A, B, C, D))
