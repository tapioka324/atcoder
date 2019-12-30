# -*- coding: utf-8 -*-

s = input()
k = int(input())

if len(s) < k:
    print(0)
    exit()

ans = list()
for i in range(len(s) - k + 1):
    ans.append(s[i:i + k])

print(len(set(ans)))
