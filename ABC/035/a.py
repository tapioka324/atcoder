# -*- coding: utf-8 -*-

# input
W, H = map(int, input().split())

# solve & output
print('4:3' if 3 * W == 4 * H else '16:9')
