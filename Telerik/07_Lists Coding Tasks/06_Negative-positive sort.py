# Description
# Write a program that moves all negative numbers to the beginning 
# and all positive ones to the end, without changing the order of positive negative

# Input
# On a single line you will receive numbers separated by space
# Output
# Print the sorted numbers
# Constraints
# The input will consist of valid integer numbers

numbers_list = input().split(" ")
negative_list = []
positive_list = []
index = 0

for char in numbers_list:
    if int(char) < 0:
        negative_list.insert(index , char)
        index += 1
    elif int(char) >= 0:
        positive_list.insert(index , char)
        index += 1

negative_list.extend(positive_list)        
print(" ".join(map(str ,negative_list)))