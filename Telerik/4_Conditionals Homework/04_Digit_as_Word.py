# Description
# Write a program that read a digit [0-9] from the console, 
# and depending on the input, shows the digit as a word (in English).

# Print "not a digit" in case of invalid input.
# Use a switch statement.
# Input
# The input consists of one line only, which contains the digit.
# Output
# Output a single line - should the input be a valid digits, 
# print the english word for the digits. Otherwise, print "not a digit".
# Constraints
# The input will never be an empty line.

digit_input = input()

if digit_input == "0":
    print("zero")
elif digit_input == "1":
    print("one")
elif digit_input == "2":
    print("two")
elif digit_input == "3":
    print("three")
elif digit_input == "4":
    print("four")
elif digit_input == "5":
    print("five")
elif digit_input == "6":
    print("six")
elif digit_input == "7":
    print("seven")
elif digit_input == "8":
    print("eight")
elif digit_input == "9":
    print("nine")
else:
    print("not a digit")