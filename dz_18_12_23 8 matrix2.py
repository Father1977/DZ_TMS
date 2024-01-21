import random

m = int(input("Введите размер матрицы, значение M (число столбцов): "))
n = int(input("Введите размер матрицы, значение N (число строк): "))


def min_max_matrix(m, n):
    matrix = [[random.randrange(0, 15) for _ in range(m)] for _ in range(n)]
    for im in range(n):
        print(matrix[im])
    max_value = max(map(max, matrix))
    min_value = min(map(min, matrix))
    max_index = matrix.index(max(matrix))
    min_index = matrix.index(min(matrix))

    print(f"Значение максимального элемента матрицы M*N: {max_value}")
    print(f"Значение мнимального элемента матрицы M*N: {min_value}")
    print(f"Индекс максимального элемента матрицы M*N: {max_index}")
    print(f"Индекс минимального элемента матрицы M*N: {min_index}")


min_max_matrix(m, n)
