class StudentWork:
    def __init__(self):
        try:
            number = int(input("Введіть номер студента (1-5): "))
            match number:
                case 1:
                    self.student1()
                case 2:
                    self.student2()
                case 3:
                    self.student3()
                case 4:
                    self.student4()
                case 5:
                    self.student5()
                case _:
                    print("We are just 5 here :()")
        except ValueError:
            print("Code has shited itself :_(")
    
    """==================================================================================="""

    def student1(self): # by Mark Shaposhnik (marguuss)
        user_input = input("chat.txt: ")
        with open('chat.txt', 'w') as file:
            file.write(user_input + '\n')
        print("I am done here))")

    def student2(self): # by Kim Yelyzaveta
        user_input = input("Введіть текст для доконання в файл chat.txt: ")
        with open('chat.txt', 'a') as file:  # Використовуємо режим додавання 'a'
            file.write(user_input + '\n')
        print("Додатковий текст успішно записан в файл.")


    def student3(self): # By Diachenko Vitalii
        predefined_text = "\nBeacause Python it's my life :)"
        with open('chat.txt', 'a') as file:
            file.write(predefined_text + '\n')

    def student4(self): # By Kovalenko Vadim
        print("Метод студента 4 выполнен.")
        try:
            # Операція зчитування даних із файла
            with open('chat.txt', 'r') as file:
                content = file.read()
                print("Зміст файлу:")
                print(content)
            
            # Запрос на дод.текст
            additional_text = input("Введіть додат. текст: ")
            
            # Операція запису тексту в файл
            with open('chat.txt', 'w') as file:
                file.write(content + additional_text + '\n')
            print("ТЕкст додано у файл.")
        except FileNotFoundError:
            print("Файл не знайдено, перевірте наявність файла")
        except Exception as e:
            print(f"Виникла помилка: {e}")

    def student5(self):
        print("student5 is here))")

work = StudentWork()
