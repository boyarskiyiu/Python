str_usr = str(input("Ввведите строку - "))
word = str_usr.split()
for n, w in enumerate(word, 1):
    print(n, w[1: 10])
