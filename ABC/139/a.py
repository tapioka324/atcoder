# -*- coding: utf-8 -*-

# input
S = input()
T = input()

# solve
ans = 0
for i in range(3):
    if S[i] == T[i]:
        ans += 1

# output
print(ans)
