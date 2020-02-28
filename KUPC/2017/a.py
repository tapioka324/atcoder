# -*- coding: utf-8 -*-

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)

ans = -1
for i in range(N):
    K -= A[i]
    if K <= 0:
        ans = i + 1
        break

print(ans)
