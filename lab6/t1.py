def modify_list(user_list):
    if len(user_list) >= 4:
        user_list.pop(1)
        user_list.pop(-2)
    elif len(user_list) == 3:
        user_list.pop(1)
    return user_list

user_input = input("Enter the list elements separated by space: ")
user_list = user_input.split() 

modified_list = modify_list(user_list)
print("Modified list:", modified_list)