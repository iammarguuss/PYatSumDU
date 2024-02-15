def t2_mod(x, y):
    product = 1
    for num in range(x, y + 1):
        if num % 2 != 0:
            product *= num
    return product
