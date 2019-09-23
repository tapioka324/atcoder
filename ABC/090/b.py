# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())

# solve
ans = 0
for i in range(A, B + 1):
    if str(i) == str(i)[::-1]:
        ans += 1

# output
print(ans)
