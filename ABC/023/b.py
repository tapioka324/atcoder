# -*- coding: utf-8 -*-

N = int(input())
S = input()

ans = 'b'
if S == ans:
    print(0)
    exit()

for i in range(1, N // 2 + 1):
    if i % 3 == 1:
        ans = 'a' + ans + 'c'
    elif i % 3 == 2:
        ans = 'c' + ans + 'a'
    else:
        ans = 'b' + ans + 'b'

print(N // 2 if ans == S else '-1')
