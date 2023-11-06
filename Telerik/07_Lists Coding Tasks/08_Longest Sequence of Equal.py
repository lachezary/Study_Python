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

max_length = 1
current_length = 1

input_elements = []

for i in range (input_lines):
    num = int(input())
    input_elements.append(num)
    
for i in range(1 , input_lines):
    if input_elements[i] == input_elements [i - 1]:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
        current_length = 1

if current_length > max_length:
    max_length = current_length
    
print(max_length)