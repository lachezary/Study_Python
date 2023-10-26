# Write a program that, for a given two numbers N and X, calculates the sum S = 1 + 1!/x + 2!/x2 + … + N!/xN.

# Use only one loop. Print the result with 5 digits after the decimal point.
# Each element is calculated as follows: (previous_element) * i / xi

# Output
# Output only one number - the sum of the sequence for the given N and X.

num1 = int(input())
num2 = float(input())

total_sum = 1.0
term = 1.0

for i in range(1, num1 + 1):
    term = term * i / num2
    total_sum += term


total_sum = round(total_sum, 5)
print(f"{total_sum:.5f}")
