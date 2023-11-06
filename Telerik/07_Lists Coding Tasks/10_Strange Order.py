# Write a program that orders a list of numbers in the 
# following way:

# 3,-2,1,0,-1,0,-2,1 -> -2,-1,-2,0,0,3,1,1
# You need to find out the criteria for yourself by 
# looking at the example. 
# You can also check the example below.

# Input
# On the only line of input, you will receive the numbers, 
# separated by a comma.
# Output
# Display the list with the mysterious ordering applied 
# removed, separated by a comma.

strange_list = input().split(",")
list_negatives = []
list_zeroes = []
list_positives = []
length = len(strange_list)
result_list = []

char = 0

for i in range(length):
    char = strange_list[i]
    if int(char) < 0:
        list_negatives.append(char)
    elif int(char) == 0:
        list_zeroes.append(char)
    elif int(char) > 0:
        list_positives.append(char)

result_list.extend(list_negatives)
result_list.extend(list_zeroes)
result_list.extend(list_positives)

print(",".join(map(str, result_list)))

