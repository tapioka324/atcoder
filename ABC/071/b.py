# -*- coding: utf-8 -*-

# input
S = input()

# solve
flag = False
for i in range(97, 97 + 26):
    if chr(i) not in S:
        ans = chr(i)
        flag = True
        break


# output
print(ans if flag else 'None')
