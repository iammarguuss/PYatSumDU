class StudentWork:
    def __init__(self):
        try:
            match int(input("Введите номер студента (1-5): ")):
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

    def student2(self):
        print("student2 is here))")

    def student3(self):
        print("student3 is here))")

    def student4(self):
        print("student4 is here))")

    def student5(self):
        print("student5 is here))")

work = StudentWork()