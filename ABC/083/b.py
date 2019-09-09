# -*- coding: utf-8 -*-

# input
N, A, B = map(int, input().split())

# solve
ans = 0
for i in range(1, N + 1):
    now = str(i)
    tmp = 0
    for j in range(len(now)):
        tmp += int(now[j])
    if A <= tmp and tmp <= B:
        ans += int(now)

# output
print(ans)
