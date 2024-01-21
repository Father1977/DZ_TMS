import random


def binarySearch(list, left, right, value):
    if left > right:
        return -1

    mid = (left + right) // 2

    if value == list[mid]:
        return mid

    elif value < list[mid]:
        return binarySearch(list, left, mid - 1, value)

    else:
        return binarySearch(list, mid + 1, right, value)


if __name__ == '__main__':

    spisok = []
    for i in range(10):
        spisok.append(random.randint(1, 50))
    spisok.sort()
    print(spisok)

# искомое число
value = int(input("Введите искомое число: "))

(left, right) = (0, len(spisok) - 1)

index = binarySearch(spisok, left, right, value)

if index != -1:
    print(f"Индекс позиции в списке {index}")
else:
    print("Значение не найдено.")
