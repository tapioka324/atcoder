# -*- coding: utf-8 -*-

# input
N = int(input())
p = list(map(int, input().split()))

# solve
l = sorted(p)
count = 0
for i in range(N):
    if p[i] != l[i]:
        count += 1

# output
print('YES' if count == 2 or count == 0 else 'NO')
