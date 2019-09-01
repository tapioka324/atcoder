# -*- coding: utf-8 -*-

# input
N = int(input())
H = list(map(int, input().split()))

# solve
l = list()
for i in range(N - 1):
    l.append(H[i + 1] - H[i])
tmp = 0
ans = 0
for i in range(len(l)):
    if l[i] <= 0:
        tmp += 1
        ans = max(ans, tmp)
    else:
        tmp = 0

# output
print(ans)
