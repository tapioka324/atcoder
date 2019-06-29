# -*- coding: utf-8 -*-

# input
n = int(input())
p = list(map(int, input().split()))

# solve
ans = 0
for i in range(0, n - 2):
    l = list(p[i:i + 3])
    s = sorted(l)
    if l[1] == s[1]:
        ans += 1

# output
print(ans)
