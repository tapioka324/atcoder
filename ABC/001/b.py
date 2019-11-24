# -*- coding: utf-8 -*-

m = int(input())
m /= 1000

if m < 0.1:
    print('00')
elif 0.1 <= m <= 5:
    print('{0:02d}'.format(int(m * 10)))
elif 6 <= m <= 30:
    print(int(m) + 50)
elif 35 <= m <= 70:
    print(int((m - 30) / 5) + 80)
else:
    print('89')
