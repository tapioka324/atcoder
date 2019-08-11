# -*- coding: utf-8 -*-

# input
K, X = map(int, input().split())

# solve & output
if K > 1:
    for i in range(X - K + 1, X + K):
        if i == X + K - 1:
            print(i)
        else:
            print(i, end=' ')
else:
    print(X)
