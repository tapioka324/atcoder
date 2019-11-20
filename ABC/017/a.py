# -*- coding: utf-8 -*-

# input
se = list()
for i in range(3):
    se.append(list(map(int, input().split())))

# solve
ans = 0
for i in range(3):
    ans += se[i][0] * se[i][1] * 0.1

# output
print(int(ans))
