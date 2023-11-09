# # Output
# # Print the maximal sum of consecutive numbers


line_input = int(input())
num_line = []
current_sum = -9999
last_sum = -9999
max_sum = -9999


for i in range (line_input):
    char = int(input())
    num_line.append(char)
    if last_sum < 0:
        last_sum = 0
    if i == 0:
        current_sum = char
    elif i != 0:
        current_sum = last_sum + char
        if current_sum > max_sum:
            max_sum = current_sum
    last_sum = current_sum
print(max_sum)

