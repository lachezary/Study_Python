# Input
# On the first line, you will receive the first array as a string
# On the second line, you will receive the second array as a string
# Output
# Print "first" if the first array is lexicographically smaller
# Print "second" if the second array is lexicographically smaller
# Print "equal" if the arrays are equal
# Constraints
# The strings will always be with lower case characters
# You do not need to explicitly validate the input

first_array = input()
first_value = 0
second_value = 0
second_array = input()

# for char in first_array:
#     first_value = first_value + ord(char)
# for char in second_array:
#     second_value = second_value + ord(char)
    
# if first_value < second_value:
#     print("first")
# elif first_value > second_value:
#     print("second")
# elif first_value == second_value:
#     print("equal")

first_list = list(first_array)
second_list = list(second_array)

if first_list < second_list:
    print("first")
elif first_list > second_list:
    print("second")
elif first_list == second_list:
    print("equal")
