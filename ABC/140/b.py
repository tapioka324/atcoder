# -*- coding: utf-8 -*-

# input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# solve
ans = 0
prev = 0
for i in range(N):
    now = A[i] - 1
    ans += B[now]
    if i != 0 and prev == now - 1:
        ans += C[prev]
    prev = now

# output
print(ans)
