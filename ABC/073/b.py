# -*- coding: utf-8 -*-

# input
N = int(input())
lr = [list(map(int, input().split())) for i in range(N)]

# solve
ans = 0
for i in range(N):
    ans += lr[i][1] - lr[i][0] + 1

# output
print(ans)
