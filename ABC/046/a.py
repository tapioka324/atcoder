# -*- coding: utf-8 -*-

# input
a, b, c = map(int, input().split())

# solve
if a == b and b == c:
    ans = 1
elif a == b and b != c:
    ans = 2
elif a == c and b != c:
    ans = 2
elif b == c and c != a:
    ans = 2
else:
    ans = 3

# output
print(ans)
