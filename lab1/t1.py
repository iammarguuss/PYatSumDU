a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

if 1 <= a <= 100 and 1 <= b <= 100:
    if a > b:
        X = a / b - 1
    elif a == b:
        X = -25
    else:
        X = (a**3 - 5) / a
    print(f"Value of X: {X}")
else:
    print("Values for a and b must be between 1 and 100 and positive.")
