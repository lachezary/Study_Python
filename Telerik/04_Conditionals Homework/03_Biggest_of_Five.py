# Biggest of Five
# Description
# Write a program that finds the biggest of 5 numbers, using only 5 if statements.

# Input
# Read from the standard input.

# On the first 5 lines, you will receive the 5 numbers, each on a separate line
# Output
# Print to the standard output.

# Write the biggest of the five numbers on the only output line.
# Constraints
# The five numbers will always be valid integer numbers in the range [-200, 200]. 
# You do not have to check if they are valid explicitly.

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

big_num = -200

if num5 > big_num:
    big_num = num5
if num4 > big_num:
    big_num = num4
if num3 > big_num:
    big_num = num3
if num2 > big_num:
    big_num = num2   
if num1 > big_num:
    big_num = num1

print(big_num)