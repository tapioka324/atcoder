# -*- coding: utf-8 -*-

# input
S = list()
for i in range(12):
    S.append(input())

# solve
ans = 0
for i in range(12):
    if S[i].find('r') != -1:
        ans += 1

# output
print(ans)
