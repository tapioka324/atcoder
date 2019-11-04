# -*- coding: utf-8 -*-

# input
W = input()

# solve
ans = ''
for i in range(len(W)):
    if W[i] != 'a' and W[i] != 'i' and W[i] != 'u' and W[i] != 'e' and W[i] != 'o':
        ans += W[i]

# output
print(ans)
