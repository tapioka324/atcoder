# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())

# solve
ans = 0
plug = 1
while True:
    if plug >= B:
        break
    plug += A - 1
    ans += 1

# output
print(ans)
