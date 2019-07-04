# -*- coding: utf-8 -*-

# input
N, K = map(int, input().split())
S = input()

# solve
ans = ''
for i in range(len(S)):
    ans += S[i] if i != K - 1 else S[i].lower()

# output
print(ans)
