number = int(input("Ведите трехзначное число:  "))
num_1 = number // 100
num_2 = (number % 100) // 10
num_3 = number % 10
print(num_1 + num_2 + num_3)
