import math
from t2_mod import t2_mod

# Функция для вычисления z
def calculate_z(m):
    return -math.sqrt(m)

# Основная часть программы
def main():
    m = float(input("Введите значение m: "))
    z = calculate_z(m)
    print(f"Значение z: {z}")

    x = int(input("Введите начальное значение x: "))
    y = int(input("Введите конечное значение y: "))
    product = t2_mod(x, y)
    print(f"Произведение всех нечетных чисел от {x} до {y}: {product}")

if __name__ == "__main__":
    main()
