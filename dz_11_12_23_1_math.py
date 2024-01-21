import math

# Ввод данных с клавиатуры
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
x = int(input("Введите число X: "))
# расчет формулы a)
e = int((pow(a, 2)+4))
c = int(e/4)
d = int((pow(e, 3)/4))
y = (pow(a, 2)/3) + ((pow(a, 2)+4)/b) + (math.sqrt(c)) + (math.sqrt(d))
print(f"Значение Y = {y:.2f}")
# Вывод с округлением до наибольшего целого числа
print(f"Значение Y = {math.ceil(y)}")
# Вывод с округлением до наименьшего целого числа
print(f"Значение Y = {math.floor(y)}")

print()
# расчет формулы b)
y = math.cos(x) + math.sin(x)
print(f"Значение Y в радианах = {y:.2f}")
print(f"Значение Y в градусах = {math.degrees(y):.2f}")

# расчет формулы c)

y = pow(pow(math.cos(pow(x, 2)), 2) + pow(math.sin(x*2 - 1), 2), 1/3)
print(f"Значение Y в радианах = {y:.2f}")
print(f"Значение Y в градусах = {math.degrees(y):.2f}")
print()

# расчет формулы d)
y = x*5 + (pow(x, 2) * 3) * math.sqrt(1 + pow(math.sin(x), 2))
print(f"Значение Y = {y:.2f}")
# Вывод с округлением до наибольшего целого числа
print(f"Значение Y = {math.ceil(y)}")
# Вывод с округлением до наименьшего целого числа
print(f"Значение Y = {math.floor(y)}")
