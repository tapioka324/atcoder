# -*- coding: utf-8 -*-

# input
l = list(map(int, input().split()))

# solve
if l[0] == l[1] != l[2]:
    ans = l[2]
elif l[0] == l[2] != l[1]:
    ans = l[1]
elif l[0] != l[1] == l[2]:
    ans = l[0]
else:
    ans = l[0]

# output
print(ans)
