# -*- coding: utf-8 -*-

N = int(input())
A = list(int(input()) for i in range(N))

ans = sorted(list(set(A)))

print(ans[len(ans) - 2])
