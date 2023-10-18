# You have deposited a sum into your bank account for 3 years. 
# The bank has announced an interest of 5% per year. 
# Each time the interest is calculated and added to your deposit. 
# You have to calculate the amount in your deposit for each year.

# Input
# On the only line you will receive a number (n) with the sum deposited
# Output
# You should print the amount in your deposit for each of the 3 years
# Constraints
# You must print the number with two numbers after the decimal point. 
# The rules of math for rounding apply here

deposit = float(input())

rate = 1.05
result = deposit * rate
print(f"{result:.2f}")
result = result * 1.05
print(f"{result:.2f}")
result = result * 1.05
print(f"{result:.2f}")


