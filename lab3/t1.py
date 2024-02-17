text = input("Enter a long string: ")

if len(text) >= 10:
    first_ten_chars = text[:10]
else:
    first_ten_chars = "String is too short.("

print(first_ten_chars)
