# -*- coding: utf-8 -*-

c = [input().split() for i in range(4)]

for i in c[::-1]:
    print(*i[::-1])
