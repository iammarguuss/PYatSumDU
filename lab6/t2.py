def find_top_five_max_elements(user_list):

    if len(user_list) < 5:
        return "The list does not have enough elements."

    numeric_list = [float(i) for i in user_list]    
    return sorted(numeric_list, reverse=True)[:5]

user_input = input("Enter the list elements separated by space: ")
user_list = user_input.split()

top_five_max = find_top_five_max_elements(user_list)
print("Top five maximum elements:", top_five_max)