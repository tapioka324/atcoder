# -*- coding: utf-8 -*-

# input
a, b = map(int, input().split())

# solve
ans = "Even" if ((a * b) % 2 == 0) else "Odd"

# output
print(ans)
