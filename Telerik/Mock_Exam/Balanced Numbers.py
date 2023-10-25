# A balanced number is a 3-digit number whose second digit is equal
# to the sum of the first and last digit.

# Write a program which reads and sums balanced numbers.
# You should stop when an unbalanced number is given.

# Input
# Input data is read from the standard input

# Numbers will be given
# Each one will be on a separate line
# Output
# Print to the standard output

# Constraints
# No more than 1000 numbers will be given
sum = 0

for i in range(1000):
    number = input()
    if (int(number[0]) + int(number[2])) == int(number[1]):
        sum += int(number)
    else:
        break

print(sum)
