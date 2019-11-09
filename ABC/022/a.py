# -*- coding: utf-8 -*-

# input
N, S, T = map(int, input().split())
W = int(input())
A = list()
A.append(W)
for i in range(N - 1):
    W += int(input())
    A.append(W)

# solve
ans = 0
for i in range(N):
    if S <= A[i] and A[i] <= T:
        ans += 1

# output
print(ans)
