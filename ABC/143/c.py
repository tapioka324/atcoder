# -*- coding: utf-8 -*-

# input
N = int(input())
S = input()

# solve
ans = 0
for i in range(N - 1):
    if S[i + 1] != S[i]:
        ans += 1

# output
print(ans + 1)
