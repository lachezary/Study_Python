# Input
# Read from the standard input.

# On the first line, read the number n - the number of boxes.
# Output
# Print to the standard output.

# On a single line print the difference between 
# the number of oranges and the number of apples.
# Constraints
# n can get as big as 40.

boxes_input = int(input())

apples = 0
oranges = 0


for box in range (boxes_input + 1):
    if box % 2 == 0:
        apples = apples + (box * box)
    else:
        oranges = oranges + (box * box)
        

result = apples - oranges

print(result)