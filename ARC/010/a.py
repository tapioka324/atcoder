# -*- coding: utf-8 -*-

N, M, A, B = map(int, input().split())
c = list(int(input()) for i in range(M))

flag = True
ans = 0
for i in range(M):
    ans += 1
    if N <= A:
        N += B
    if N < c[i]:
        flag = False
        break
    else:
        N -= c[i]

print('complete' if flag else ans)
