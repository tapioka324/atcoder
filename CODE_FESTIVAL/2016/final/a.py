# -*- coding: utf-8 -*-

H, W = map(int, input().split())
S = list(list(map(str, input().split())) for i in range(H))

for i in range(H):
    for j in range(W):
        if S[i][j] == 'snuke':
            print(chr(65 + j) + str(i + 1))
            break
