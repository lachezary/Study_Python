# Array Search
# Given an array of integers, some elements appear twice and others appear once. 
# Each integer is in the range of [1, N], where N is the number of elements in the array.

# Find all the integers of [1, N] inclusive that do NOT appear in this array.

# Input
# Read from the standard input:

# There is one line of input, containing N amount of integers, seperated by a comma (",")
# Output
# Print to the standard output:

# There is one line of output, containing the sorted integers, seperated by a comma (",")
# Constraints
# N will always be in the range of [5, 1000]

input_line = input().split(",")
sorted_line = list(map(int, input_line))
sorted_line.sort()
start_char = sorted_line[0]
length = len(sorted_line)
result = []

for i in range(start_char, start_char + length):
    if i not in sorted_line:
        result.append(i)

print(",".join(map(str, result)))


