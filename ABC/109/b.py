# -*- coding: utf-8 -*-

# input
N = int(input())
W = list()
for i in range(N):
    W.append(input())

# solve
ans = True
if len(set(W)) != N:
    ans = False
else:
    for i in range(N - 1):
        if W[i][-1] != W[i + 1][0]:
            ans = False

# output
print('Yes' if ans else 'No')
