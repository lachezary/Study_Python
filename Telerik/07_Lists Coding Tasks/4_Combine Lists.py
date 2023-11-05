# Write a program that reads two lists of numbers and combines 
# them by alternatingly taking elements:

# combine 1,2,3 and 7,8,9 -> 1,7,2,8,3,9
# you can assume that the input lists will have the same length.
# Print the resulting combined list to the output, separating elements with a comma.

# Input
# On the first line you will receive the first list.
# On the second line -> 2nd list.
# Output
# On the only line of output, print all the numbers in format n1,n2,n3,..n

first_list = input().split(",")
second_list = input().split(",")
combined_list = []

length = len(first_list)

for i in range (length):
    combined_list.append(first_list[i])
    combined_list.append(second_list[i])

print(','.join(map(str, combined_list))) 
