# -*- coding: utf-8 -*-

# input
N, X = map(int, input().split())
L = list(map(int, input().split()))

# solve
D = [0]
for i in range(N):
    D.append(D[i] + L[i])

ans = [e for e in D if e <= X]

# output
print(len(ans))
