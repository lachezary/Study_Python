# Remove Duplicates
# Write a program that removes all duplicates from a 
# list of elements.

# 1,2,2,2,4,7 -> 1,2,4,7.
# Maintain the relative order of the remaining items.

# Input
# On the only line of input, you will receive the elements, 
# separated by a comma.
# Output
# Display the list with the duplicates removed, separated 
# by a comma.
# Constraints
# 1 <= list.length <= 20

dupe_line = input().split(",")
result_line = []
length = len(dupe_line)

for i in range(length - 1):
    if dupe_line[i] == dupe_line[i+1]:
        continue
    else:
        if dupe_line[i] in result_line:
            continue
        else:
            result_line.append(dupe_line[i])

if dupe_line[-1] not in result_line:
    result_line.append(dupe_line[-1])


print(",".join(map(str, result_line)))