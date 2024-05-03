try:
    with open('TF8_1', 'w', encoding='utf-8') as file:
        file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit123.\n")
        file.write("Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n")
        file.write("Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n")
except IOError as e:
    print(f"Err: {e}")

try:
    with open('TF8_1', 'r', encoding='utf-8') as file:
        content = file.read()
    content = ''.join([ch for ch in content if not ch.isdigit()])

    output_lines = []
    for i in range(0, len(content), 10):
        line_number = len(output_lines) + 1
        output_lines.append(f"{line_number:5} {content[i:i+10]}\n")

    with open('TF8_2', 'w', encoding='utf-8') as file:
        file.writelines(output_lines)
except IOError as e:
    print(f"Err: {e}")

try:
    with open('TF8_2', 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
except IOError as e:
    print(f"Err: {e}")
