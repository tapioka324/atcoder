# -*- coding: utf-8 -*-

# input
H, W = map(int, input().split())
C = [list(map(str, input().split())) for i in range(H)]

# solve & output
for i in range(H):
    ans = C[i] * 2
    for j in range(2):
        print(ans[j])
