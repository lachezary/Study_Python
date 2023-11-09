
# Output
# Print all two numbers (pairs) that equal the target sum (N) separated with a comma (",")
# If there are no pairs, print "no pairs"
# Constraints
# All numbers will be valid integers


target_sum = int(input())

line_input = input().split(" ")

int_line = list(map(int, line_input))
counter = 0

for start_of_pair in int_line:
    for end_of_pair in int_line:
        if start_of_pair + end_of_pair == target_sum:
            print(f"{start_of_pair},{end_of_pair}")
            counter += 1
            int_line.pop(start_of_pair)
            int_line.pop(end_of_pair)

if counter == 0:
    print("no pairs")
    
