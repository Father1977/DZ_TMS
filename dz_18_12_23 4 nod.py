num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))


def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


itog = nod(num_1, num_2)

print(f"Наибольший общий делитель числа {num_1} и числа {num_2} равен {itog}")
