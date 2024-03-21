phonebook = {
    "Ivanenko": "123-45-67",
    "Petrenko": "234-56-78",
    "Sydorenko": "345-67-89",
    "Kovalenko": "456-78-90",
    "Shevchenko": "567-89-01",
    "Lysenko": "678-90-12",
    "Hryhorenko": "789-01-23",
    "Kozachenko": "890-12-34",
    "Melnychenko": "901-23-45",
    "Fedorenko": "012-34-56",
    "Zhuk": "098-76-54",
    "Bondar": "210-98-76",
    "Tkachenko": "321-09-87"
}

def print_phonebook(phonebook):
    for name, phone in phonebook.items():
        print(f"{name}: {phone}")

def add_entry(phonebook, name, phone):
    if name in phonebook:
        print(f"Entry for {name} already exists.")
    else:
        phonebook[name] = phone
        print(f"Entry for {name} successfully added.")

def remove_entry(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        print(f"Entry for {name} successfully removed.")
    else:
        print(f"Entry for {name} not found.")

def print_sorted(phonebook):
    for name in sorted(phonebook):
        print(f"{name}: {phonebook[name]}")

def find_phone_by_name(phonebook, name):
    return phonebook.get(name, "Phone number for the given name not found.")

def find_name_by_phone(phonebook, phone):
    for name, phone_number in phonebook.items():
        if phone_number == phone:
            return name
    return "Name for the given phone number not found."

print_phonebook(phonebook)
print("\nSorted output:")
print_sorted(phonebook)
print("\nFinding phone by name 'Ivanenko':")
print(find_phone_by_name(phonebook, "Ivanenko"))
print("\nFinding name by phone number '123-45-67':")
print(find_name_by_phone(phonebook, "123-45-67"))