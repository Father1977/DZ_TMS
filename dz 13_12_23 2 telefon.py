name = input("Меня зовут: ")
cost_telephone = int(input(f"{name}, введите стоимость телефона = "))
save_rubles = int(input(f"{name}, какую сумму Вы планируете откладывать? "))
days = 0
money = 0
while money < cost_telephone:
    days += 1
    if days % 7 != 0:
        money += save_rubles
print(f"{name}, такими темпами Вы сможете накопить на Ваш новый телефон за {days} дней или {(days/7):.2f} недель!")
