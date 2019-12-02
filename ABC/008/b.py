# -*- coding: utf-8 -*-

N = int(input())
S = list(input() for i in range(N))

ans = [0] * N
for i in range(N):
    for j in range(i, N):
        if S[i] == S[j]:
            ans[i] += 1

print(S[ans.index(max(ans))])
