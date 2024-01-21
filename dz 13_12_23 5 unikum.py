import random

N = 10
arr = [random.randrange(50) for i in range(N)]
print(*arr)

setarr = set(arr)

for item in setarr:
    count = arr.count(item)
    if count > 1:
        print(f"Элемент {item} встречается {count} раз")
        exit()
else:
    print("Все элементы уникальные!")
