# Write a program that, that finds the three largest numbers in a
# sequence and prints them in descending order in the following format:

# {largest}, {second_largest} and {third_largest}.

# See the example for clarity

# Input
# On the first line you will receive one number - N - the count of numbers to follow.
# On the next N lines you will receive the sequence of numbers, each on a new line.
# Output
# Output the three largest numbers in the already described format.
# Constraints
# 3 <= N <= 20
# -500 <= each number <= 500


largest = -500
second_largest = -500
third_largest = -500

nums = int(input())

for i in range(nums):
    digit_input = int(input())
    if digit_input > largest:
        third_largest = second_largest
        second_largest = largest
        largest = digit_input
    elif digit_input > second_largest:
        third_largest = second_largest
        second_largest = digit_input
    elif digit_input > third_largest:
        third_largest = digit_input

print(f"{largest}, {second_largest} and {third_largest}")
