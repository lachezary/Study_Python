# Write a program that finds the length of the maximal sequence of
# equal elements in an array of N integers.

# Input
# On the first line you will receive the number N
# On the next N lines the numbers of the array will be given
# Output
# Print the length of the maximal sequence
# Constraints
# 1 <= N <= 1024


input_lines = int(input())
old_num = 0
num = 0
counter = 0
old_counter = 0

for i in range(input_lines):
    num = int(input())
    if counter == 0 and old_counter == 0:
        old_num = num
    elif num == old_num:
        counter += 1
    elif num != old_num:
        old_counter = counter
        old_num = num
        counter = 0

