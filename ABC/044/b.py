# -*- coding: utf-8 -*-

# input
w = input()

# solve
ans = True
for i in range(len(w)):
    if len(w) != 0:
        tmp = w[0]
        count = w.count(tmp)
        w = w.replace(tmp, '')
        if count % 2 != 0:
            ans = False
    else:
        break

# output
print('Yes' if ans else 'No')
