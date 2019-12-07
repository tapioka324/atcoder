# -*- coding: utf-8 -*-

S = input()

ans = False
if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
    ans = True

print('Bad' if ans else 'Good')
