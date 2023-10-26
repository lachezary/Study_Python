# Description
# Write a program that enters 3 real numbers and prints them sorted in descending order.

# Use nested if statements.
# Don’t use arrays and the built-in sorting functionality.
# Input
# On the first three lines, you will receive the three numbers, each on a separate line.
# Output
# Output a single line on the console - the sorted numbers, separated by a white space
# Constraints
# The three numbers will always be valid integer numbers in the range [-1000, 1000]


num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(f"{num1} {num2} {num3}")
    else:
        print(f"{num1} {num3} {num2}")
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(f"{num2} {num1} {num3}")
    else:
        print(f"{num2} {num3} {num1}")
elif num3 >= num2 and num3 >= num1:
    if num2 >= num1:
        print(f"{num3} {num2} {num1}")
    else:
        print(f"{num3} {num1} {num2}")