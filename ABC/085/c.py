# -*- coding: utf-8 -*-

# input
N, Y = map(int, input().split())

# solve
ans = [-1] * 3
for x in range(N + 1):
    for y in range(N + 1):
        z = N - x - y
        if 10000 * x + 5000 * y + 1000 * z == Y and z >= 0:
            ans = [x, y, z]
            break

# output
print(*ans)
