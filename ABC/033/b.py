# -*- coding: utf-8 -*-

# input
N = int(input())
S = list()
P = list()
for i in range(N):
    s, p = map(str, input().split())
    S.append(s)
    P.append(int(p))

# solve
majority = sum(P) / 2
ans = -1
for i in range(N):
    if P[i] > majority:
        ans = i

# output
print(S[ans] if ans != -1 else 'atcoder')
