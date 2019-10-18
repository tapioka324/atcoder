# -*- coding: utf-8 -*-

# input
N = int(input())

# solve & output
if N <= 59:
    print('Bad')
elif 60 <= N and N <= 89:
    print('Good')
elif 90 <= N and N <= 99:
    print('Great')
else:
    print('Perfect')
