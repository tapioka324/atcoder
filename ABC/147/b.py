# -*- coding: utf-8 -*-

S = input()

ans = 0
for i in range(len(S)):
    if S[i] != S[::-1][i]:
        ans += 1

print(ans // 2)
