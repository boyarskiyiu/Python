print("вариант с списком -list")
mount = int(input("введите номнер месяца- "))
season_list = ["зима", "весна", "лето", "осень"]
if mount == 12 or mount >= 1 and mount <= 2:
    print(season_list[0])
elif mount >= 3 and mount <= 5:
    print(season_list[1])
elif mount >= 6 and mount <= 8:
    print(season_list[2])
elif mount >= 9 and mount <= 12:
    print(season_list[3])
else:
    print("Месяца с таким номером не существует")

print("вариант со словарем -dict")
mount = int(input("введите номнер месяца- "))
season_dict = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
if mount == 12 or mount >= 1 and mount <= 2:
    print(season_dict.get(1))
elif mount >= 3 and mount <= 5:
    print(season_dict.get(2))
elif mount >= 6 and mount <= 8:
    print(season_dict.get(3))
elif mount >= 9 and mount <= 12:
    print(season_dict.get(4))
else:
    print("Месяца с таким номером не существует")
