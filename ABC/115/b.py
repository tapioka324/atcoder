# -*- coding: utf-8 -*-

# input
N = int(input())
p = list()
for _ in range(N):
    p.append(int(input()))

# solve
p.sort()
ans = int(p[-1] / 2 + sum(p[:-1]))

# output
print(ans)
