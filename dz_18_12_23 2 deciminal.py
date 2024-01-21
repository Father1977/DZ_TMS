num_decimal = int(input("Введите число: "))
list_decimal = []


def convert(b):
    if b == 0:
        return list_decimal
    dig = b % 2
    list_decimal.append(dig)
    convert(b // 2)


list_decimal.reverse()
convert(num_decimal)
print(f"Двоичная форма числа {num_decimal}:")
for i in list_decimal:
    print(i, end="")

print()
# при помощи встроеной функции bin
print(f"Двоичная форма числа {num_decimal} - {bin(num_decimal)}")
