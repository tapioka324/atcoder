# -*- coding: utf-8 -*-

# input
N = int(input())

# solve
ans = 0
for i in range(1, N + 1):
    if len(str(i)) % 2 != 0:
        ans += 1

# output
print(ans)
