# -*- coding: utf-8 -*-

# input
S = input()

# solve
is_YYMM = False
is_MMYY = False

if '00' <= S[:2] and ('01' <= S[2:] and S[2:] <= '12'):
    is_YYMM = True
if ('01' <= S[:2] and S[:2] <= '12') and '00' <= S[2:]:
    is_MMYY = True

# output
if is_YYMM and is_MMYY:
    print('AMBIGUOUS')
elif is_YYMM:
    print('YYMM')
elif is_MMYY:
    print('MMYY')
else:
    print('NA')
