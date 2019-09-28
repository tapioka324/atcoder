# -*- coding: utf-8 -*-

# input
L, H = map(int, input().split())
N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())

# solve & output
for i in range(N):
    if A[i] < L:
        print(L - A[i])
    elif L <= A[i] and A[i] <= H:
        print('0')
    else:
        print('-1')
