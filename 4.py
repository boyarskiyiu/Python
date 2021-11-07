n = int(input("введите целое положительное число : "))
maxn=0
while n % 10 >= maxn:
  maxn = n % 10
  n = n // 10
print("максимальная цифра в числе -", maxn)

nn = input("введите целое положительное число : ")
nn = list(nn)
maxn = max(nn)
print("максимальная цифра в числе -", maxn)
