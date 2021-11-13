reiting = [7, 5, 3, 3, 2]
print("Рейтинг", reiting)
n = int(input("Введите число - "))
for i in range(len(reiting)):
    if reiting[i] == n:
        reiting.insert(i + 1, n)
        break
    elif reiting[0] < n:
        reiting.insert(0, n)
    elif reiting[-1] > n:
        reiting.append(n)
    elif reiting[i] > n and reiting[i + 1] < n:
        reiting.insert(i + 1, n)
print("Новый рейтинг", reiting)
