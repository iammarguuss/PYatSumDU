import random
import string
import matplotlib.pyplot as plt
import numpy as np

def generate_contacts(num_contacts=100):
    contact_book = {}
    for _ in range(num_contacts):
        name = ''.join(random.choices(string.ascii_uppercase, k=2))
        phone_number = ''.join(random.choices(string.digits, k=4))
        contact_book[name] = phone_number
    return contact_book

contacts = generate_contacts()

print("Generated Contacts:")
for name, phone in contacts.items():
    print(f"{name}: {phone}")

digit_counts = {}
for phone_number in contacts.values():
    first_digit = phone_number[0]
    if first_digit in digit_counts:
        digit_counts[first_digit] += 1
    else:
        digit_counts[first_digit] = 1

labels = list(digit_counts.keys())
sizes = list(digit_counts.values())
colors = plt.cm.viridis(np.linspace(0, 1, len(labels)))  

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal') 

plt.title('Распределение первой цифры номеров телефонов')
plt.show()
