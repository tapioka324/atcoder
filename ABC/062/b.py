# -*- coding: utf-8 -*-

# input
H, W = map(int, input().split())
a = [list(map(str, input().split())) for i in range(H)]

# solve & output
for i in range(H + 2):
    if i == 0 or i == H + 1:
        for _ in range(W + 2):
            if _ != W + 1:
                print('#', sep='', end='')
            else:
                print('#', sep='')
    else:
        for j in range(3):
            if j == 0:
                print('#', sep='', end='')
            elif j == 2:
                print('#', sep='')
            else:
                print(a[i - 1][0], sep='', end='')
