# -*- coding: utf-8 -*-

S = input()

d = {
    'O': '0',
    'D': '0',
    'I': '1',
    'Z': '2',
    'S': '5',
    'B': '8'
}

ans = ''
for i in range(len(S)):
    if S[i] in d:
        ans += d[S[i]]
    else:
        ans += S[i]

print(ans)
