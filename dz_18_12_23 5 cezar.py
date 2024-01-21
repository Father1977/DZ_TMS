alphavit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
while True:
    print("Введите Ш чтобы зашифровать сообщение, Р чтобы расшифровать и В чтобы выйти")
    menu = input(">>> ").lower()
    if menu == "в":
        break
    elif not (menu == "ш" or menu == "р"):
        continue
    output = ""
    message = input("Введите строку для шифрования: ").lower()
    key = int(input("Введите цифровой ключ для шифрования: "))
    if menu == "р":
        key *= -1
    for letter in message:
        if letter in alphavit:
            t = alphavit.find(letter)
            new_key = (t + key) % len(alphavit)
            output += alphavit[new_key]
        else:
            output += letter
    print(f"Результат: {output}")
