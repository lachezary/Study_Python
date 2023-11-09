# Given an array integers, write a program that moves all of 
# the zeroes to the end of it, while maintaining the relative 
# order of the non-zero elements.

# Input
# Read from the standard input:

# There is one line of input, containing 
# N amount of integers, seperated by a comma (",")
# Output
# Print to the standard output:

# There is one line of outpit, containing the sorted 
# integers, seperated by a comma (",")
# Constraints
# 5 <= N <= 1000

start_line = input().split(",")
sorted_line = start_line.copy()

for i in range(len(start_line) - 1, -1, -1):
    if start_line[i] == "0":
        sorted_line.pop(i)
        sorted_line.append("0")

print(",".join(map(str, sorted_line)))