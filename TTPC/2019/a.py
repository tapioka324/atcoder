A, B, T = map(int, input().split())
diff = B - A
while B < T:
    B += diff
print(B)
