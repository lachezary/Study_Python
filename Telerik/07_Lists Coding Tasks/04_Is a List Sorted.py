# Write a program that checks if a list is already sorted. 
# For a list to be sorted, the next element must NOT 
# be smaller than the previous one.

# Input
# On the first line - you will receive a number N.
# On the next N lines, you will receive a list of 
# numbers, separated by a comma
# Output
# There are N lines of output
# for each list you receive, 
# print 'true' if sorted or 'false' otherwise.

input_lines = int(input())
line_correct = True

for lines in range(input_lines):
    new_line = input().split(",")
    for i in range (len(new_line)):
        if new_line[i] > new_line[i+1]:
            line_correct = False
            break

if line_correct:
    print("All lines are correctly formatted.")
else:
    print("Not all lines are correctly formatted.")