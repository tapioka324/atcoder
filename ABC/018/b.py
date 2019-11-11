# -*- coding: utf-8 -*-

# input
S = input()
N = int(input())
lr = list()
for i in range(N):
    lr.append(list(map(int, input().split())))

# solve
tmp = S
for i in range(N):
    reverse = tmp[lr[i][0] - 1:lr[i][1]]
    ans = tmp[0:lr[i][0] - 1] + reverse[::-1] + tmp[lr[i][1]::]
    tmp = ans

# output
print(ans)
