import time
import random

start = time.time()
num_1 = random.randint(0, 10)
user_input = input("Введите число от 0 до 10: ")
if user_input.isdigit() is True:
    num_2 = int(user_input)
else:
    print("Не верно введено значение")
    exit()
if num_1 == num_2:
    print("Верно")
else:
    print(":-(")
end = time.time()
time_end = end - start
print(f"Время работы програмы {time_end} секунд")
