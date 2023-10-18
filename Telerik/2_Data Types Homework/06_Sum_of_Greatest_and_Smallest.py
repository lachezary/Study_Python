# Sum of greatest and smallest
# Write a program that reads 3 numbers (each number will be on a separate/new line), 
# calculates and prints the sum of the greatest and smallest of them.

# Input
# Read from the standard input

# Exactly 3 numbers. Each number will be on a separate line.
# Output
# Print on the standard output.

num1 = int(input())
num2 = int(input())
num3 = int(input())

big_num = max(num1, num2, num3)
small_num = min(num1, num2, num3)

sum = big_num + small_num
print(sum)