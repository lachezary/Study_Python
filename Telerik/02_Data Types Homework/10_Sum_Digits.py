# Write a program that reads a four-digit number and displays the sum of its digits

# 1213 => 1 + 2 + 1 + 3 = 7
# 2346 => 2 + 3 + 4 + 6 = 15
# Input
# On the first line, you will receive the four-digit number N
# Output
# On the only line of output, print the sum of digits
# Constraints
# 1000 <= N <= 9999
# Input

num = int(input())

num1 = num // 1000
num2 = (num // 100) % 10
num3 = (num // 10) % 10
num4 = num % 10

sum = num1 + num2 + num3 + num4

print(sum)

