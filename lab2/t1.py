import math

# Функция для вычисления z
def calculate_z(alpha):
    return (math.sqrt(2) / 2) * math.sin(alpha / 2)

# Функция для вычисления количества амеб через n часов
def calculate_amebas(n):
    return 2 ** n

# Запрос ввода от пользователя для вычисления z
alpha = float(input("Введите значение угла α (в радианах) для вычисления z: "))
z = calculate_z(alpha)
print(f"Значение z: {z}")

# Запрос ввода от пользователя для вычисления количества амеб
n = int(input("Введите количество часов n для вычисления количества амеб: "))
amebas = calculate_amebas(n)
print(f"Количество амеб через {n} часов: {amebas}")