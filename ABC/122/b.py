# -*- coding: utf-8 -*-

S = input()

ans = 0
for i in range(len(S)):
    tmp = 0
    if S[i] in ('A', 'C', 'G', 'T'):
        tmp += 1
        for j in range(i + 1, len(S)):
            if S[j] in ('A', 'C', 'G', 'T'):
                tmp += 1
            else:
                i = j
                ans = max(tmp, ans)
                break
        ans = max(tmp, ans)

print(ans)
