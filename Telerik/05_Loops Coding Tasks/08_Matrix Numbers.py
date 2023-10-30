# Write a program that reads from the console a positive integer number N and prints a matrix
# like in the examples below. Use two nested loops.

# Input
# The input will always consist of a single line, which contains the number N
# Output
# See the examples

row = int(input())
col = row
digits = 1
start = 1

for col in range(1, col+1):
    for digits in range(col, row+1):
        print(digits, end=" ")
    print("")
    digits += 1
    row += 1
