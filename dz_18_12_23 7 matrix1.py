import random

m = int(input("Введите размер матрицы, значение M (число столбцов): "))
n = int(input("Введите размер матрицы, значение N (число строк): "))

matrix = [[random.randrange(0, 10) for i in range(m)] for j in range(n)]
for im in range(n):
    print(matrix[im])
