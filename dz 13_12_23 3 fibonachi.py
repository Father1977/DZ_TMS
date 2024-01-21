fibon = int(input("Укажите количество чисел ряда Фибоначчи: "))
fibon_1 = 1
fibon_2 = 1
print(fibon_1, fibon_2, end=" ")

for i in range(2, fibon):
    fibon_1, fibon_2 = fibon_2, fibon_1 + fibon_2
    print(fibon_2, end=" ")
