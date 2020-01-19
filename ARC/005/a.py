# -*- coding: utf-8 -*-

N = int(input())
W = list(map(str, input().split()))

ans = 0
for i in range(N):
    if i == N - 1:
        W[i] = W[i].replace('.', '')
    if W[i] == 'TAKAHASHIKUN' or W[i] == 'Takahashikun' or W[i] == 'takahashikun':
        ans += 1

print(ans)
