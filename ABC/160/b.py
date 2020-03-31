X = int(input())
a = X // 500
X %= 500
print(1000 * a + 5 * (X // 5))
