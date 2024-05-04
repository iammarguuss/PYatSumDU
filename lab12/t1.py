import json
import random
import string

contact_book = {}
for _ in range(10):
    name = ''.join(random.choices(string.ascii_uppercase, k=2))
    phone_number = ''.join(random.choices(string.digits, k=4))
    contact_book[name] = phone_number

print("Contacts:")
print(json.dumps(contact_book, indent=4))

while True:
    search_input = input("Enter name or phone: ")
    if search_input.isdigit() and len(search_input) == 4:
        found = False
        for name, phone_number in contact_book.items():
            if phone_number == search_input:
                print(f"Name: {name}, Phone: {phone_number}")
                found = True
                break
        if not found:
            print("Phone not found.")
    elif len(search_input) == 2 and search_input.isalpha():
        found = False
        for name, phone_number in contact_book.items():
            if name == search_input:
                print(f"Name: {name}, Phone: {phone_number}")
                found = True
                break
        if not found:
            print("Name not found.")
    else:
        print("Invalid input.")