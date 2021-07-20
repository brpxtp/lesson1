while True:
    duration = int(input("Введите количество секунд: "))
    min = duration // 60
    hour = duration // 3600
    day = duration // 86400
    if duration > 60 and duration <= 3600:
        print(f"{min} минут {duration%60} секунд")
    elif duration > 3600 and duration <= 86400:
        print(f"{hour} час {duration%3600//60} минут {duration%60} секунд")
    elif duration > 86400:
        print(f"{day} дней {hour%24} час {duration%3600//60} минут {duration%60} секунд")
    else:
        print(f"{duration} секунд")

