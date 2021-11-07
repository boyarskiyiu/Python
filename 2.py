ts = int(input("введите время в секундах : "))
hour = int(ts / 3600)
ts = ts - hour * 3600
mint = int(ts / 60)
ts = ts - mint * 60
second = int(ts)
print("время:", hour, ":", mint, ":", second)
