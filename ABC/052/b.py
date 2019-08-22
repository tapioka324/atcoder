# -*- coding: utf-8 -*-

# input
N = int(input())
S = input()

# solve
ans = 0
tmp = 0
for i in range(N):
    if S[i] == 'I':
        tmp += 1
    else:
        tmp -= 1
    ans = max(ans, tmp)

# output
print(ans)
