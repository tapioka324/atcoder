s = input()
print('yes' if sorted(s[:4]) == sorted(s[5:7] + s[8:]) else 'no')
