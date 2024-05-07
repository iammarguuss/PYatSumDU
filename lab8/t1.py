students = {}

def add_student(group_number, full_name, course, grades):
    students[full_name] = {
        'Group Number': group_number,
        'Course': course,
        'Grades': grades
    }

add_student('IN-23', 'Mark Shaposhnik', 2, [9,8,7,8,9,8,7,6,9,10]) #First dictionary assembly, no comments yet))
add_student('IN-23', 'Kim Yelyzaveta', 6, [4,9,2,7,3,6,4,3,5,7]) #дана інформація не зберігається надійно
add_student('IN-23', 'Vitalii Diachenko', 2, [9,8,7,8,9,8,7,6,9,10]) #Дяченко
print(students)
