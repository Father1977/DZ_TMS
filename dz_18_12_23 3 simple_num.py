number = int(input("Введите число: "))


def check_simple(simple_num):
    if simple_num < 2:
        return False
    for i in range(2, int(simple_num ** 0.5) + 1):
        if simple_num % i == 0:
            return False
    return True


if check_simple(number):
    print(f"{number} - простое число")
else:
    print(f"{number} - не является простым числом")
