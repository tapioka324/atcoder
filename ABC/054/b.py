# -*- coding: utf-8 -*-

N, M = map(int, input().split())
A = list(list(input()) for i in range(N))
B = list(list(input()) for i in range(M))

ans = False
for i in range(N):
    for j in range(N):
        if i + M - 1 >= N or j + M - 1 >= N:
            continue
        match = True
        for y in range(M):
            for x in range(M):
                if A[i + y][j + x] != B[y][x]:
                    match = False
        if match:
            ans = True

print('Yes' if ans else 'No')
