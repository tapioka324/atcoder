S = input()
if S[2] == 'B':
    ans = 'Bachelor'
elif S[2] == 'M':
    ans = 'Master'
else:
    ans = 'Doctor'
print(ans ,S[:2])
