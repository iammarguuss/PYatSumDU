students = {}

def add_student(group_number, full_name, course, grades):
    students[full_name] = {
        'Group Number': group_number,
        'Course': course,
        'Grades': grades
    }

add_student('IN-23', 'Mark Shaposhnik', 2, [9,8,7,8,9,8,7,6,9,10]) #First dictionary assembly, no comments yet))

print(students)
