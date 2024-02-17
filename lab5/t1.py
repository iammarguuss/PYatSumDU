array_input = input("Enter the array elements separated by space: ")

array = [int(item) for item in array_input.split()]

min_element = min(array)

print("The minimum element in the array is:", min_element)