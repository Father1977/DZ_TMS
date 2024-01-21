import math as mt

# Именуем планеты
name_planet_1 = input("Введите название первой планеты: ")
name_planet_2 = input("Введите название второй планеты: ")
# радиусы планет 1 и 2
r_planet_1 = float(input(f"Введите радиус орбиты планеты {name_planet_1} (млн. км): "))*1000000
r_planet_2 = float(input(f"Введите радиус орбиты планеты {name_planet_2} (млн. км): "))*1000000
# орбитальные скорости планет 1 и 2
v_planet_1 = float(input(f"Введите орбитальную скорость планеты {name_planet_1} (км/ч): "))
v_planet_2 = float(input(f"Введите орбитальную скорость планеты {name_planet_2} (км/ч): "))
# находим длину года на планете 1 в днях
l_planet_1 = round(((2*r_planet_1*mt.pi)/v_planet_1)/(60*60*24))
# находим длину года на планете 2 в днях
l_planet_2 = round(((2*r_planet_2*mt.pi)/v_planet_2)/(60*60*24))
# выводим результат
print(f"""Длина года на планете {name_planet_1} равна {l_planet_1} Земных суток, \
длина года на планете {name_planet_2} - {l_planet_2} Земных суток""")
# сравниваем полученные значения для определения на какой планете длина года больше или они равны
if l_planet_1 > l_planet_2:
    print(f"Длина года на планете {name_planet_1} больше чем длина года на планете {name_planet_2} на \
{l_planet_1 - l_planet_2} Земных суток")
elif l_planet_1 == l_planet_2:
    print(f"Длина года на планете {name_planet_1} и {name_planet_2} - равны")
else:
    print(f"Длина года на планете {name_planet_2} больше чем длина года на планете {name_planet_1} на \
{l_planet_2 - l_planet_1} Земных суток")
