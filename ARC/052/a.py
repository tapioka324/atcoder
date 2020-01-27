# -*- coding: utf-8 -*-

S = input()

ans = ''
for s in S:
    if '0' <= s <= '9':
        ans += s

print(ans)
