
# Output
# Print all two numbers (pairs) that equal the target sum (N) separated with a comma (",")
# If there are no pairs, print "no pairs"
# Constraints
# All numbers will be valid integers


target_sum = int(input())

line_input = input().split(" ")

int_line = list(map(int, line_input))
counter = 0

for i in range(len(int_line)):
    for j in range(i + 1, len(int_line)):
        if int_line[i] + int_line[j] == target_sum:
            print(f"{int_line[i]},{int_line[j]}")
            counter += 1

if counter == 0:
    print("no pairs")
