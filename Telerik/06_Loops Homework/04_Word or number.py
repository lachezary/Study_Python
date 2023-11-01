# Description
# Write a program that reads from the console and checks 
# if the input is a number or a word.

# If the input is a word, it should be reversed.
# If it is a number add 1 to it.
# Input
# The input is text on a single line (without intervals)
# If the input is a word it won't contain any digits!
# Output
# Print on a single line the reversed text 
# or increased by 1 number


input_data = input()
result = ""

if input_data[-1].isdigit():
    input_data = float(input_data)
    input_data += 1
    if input_data % 1 != 0:
        print(input_data)
    else:
        print(int(input_data))
else:
    length = len(input_data)
    for i in range (length-1, -1 , -1):
        print(input_data[i], end="")