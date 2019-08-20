# -*- coding: utf-8 -*-

# input
N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N)]
cd = [list(map(int, input().split())) for i in range(M)]

# solve & output
for i in range(N):
    min_diff = 10 ** 9
    for j in range(M):
        diff = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        if min_diff > diff:
            min_diff = diff
            ans = j + 1
    print(ans)
