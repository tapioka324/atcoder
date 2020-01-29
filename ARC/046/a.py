# -*- coding: utf-8 -*-

N = int(input())

ans = ''
for i in range(int((N - 1) / 9 + 1)):
    ans += str((N - 1) % 9 + 1)

print(ans)
