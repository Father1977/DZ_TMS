import math

n_start = 0
n_end = 20

x = 15

value = 0.0

cos_x = math.cos(x)

for n in range(n_start, n_end):
    value += math.pow(-1, n) * ((math.pow(x, 2 * n)) / (math.factorial(2 * n)))

# Выводим cos(x) в радианах
print(f"cos(x) = {cos_x:.3f}")
# Выводим cos(x) в градусах
print(f"cos(x) = {round(math.degrees(cos_x))}")
print(f"Sum: {value:.3f}")
print(f"Diff: {(value - cos_x):.5f}")
