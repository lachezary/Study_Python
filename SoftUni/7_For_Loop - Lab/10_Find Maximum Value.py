# Input
# On the first line you will receive one number - N - the count of numbers to follow.
# On the next N lines you will receive the sequence of numbers, each on a new line.
# Output
# Output only one number - the maximum number you find
# Constraints
# 1 <= N <= 20
# -200 <= each number <= 200


nums = int(input())

old_digit = -2000

for i in range(nums):
    digit = int(input())
    if digit > old_digit:
        old_digit = digit


print(old_digit)
