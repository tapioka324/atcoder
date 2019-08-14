# -*- coding: utf-8 -*-

# input
N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(N)]

# solve
ans = 0
for i in range(N):
    sum = 0
    for j in range(M):
        sum += A[i][j] * B[j]
    sum += C
    if sum > 0:
        ans += 1

# output
print(ans)
