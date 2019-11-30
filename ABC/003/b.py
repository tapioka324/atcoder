# -*- coding: utf-8 -*-

S = input()
T = input()

ans = True
tmp = 'atcoder'
for s, t in zip(S, T):
    if s == t:
        continue
    else:
        if s == '@':
            if tmp.find(t) == -1:
                ans = False
                break
        elif t == '@':
            if tmp.find(s) == -1:
                ans = False
                break
        else:
            ans = False
            break

print('You can win' if ans else 'You will lose')
