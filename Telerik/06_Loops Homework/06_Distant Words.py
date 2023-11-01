# Examples:

# word 'bob', number = 22, distance = 3 ('b' + 'o' + 'b' = 2 + 15 + 2 = 19)
# word 'bob', number = 10, distance = 9
# Write a program that calculates the distance for each 
# string and also outputs the average distance.

# Input
# The input consists of several lines.
# T - the target number
# N - the number of words to follow
# on the next N lines - each word on a new line
# Output
# Output consists of N + 1 lines
# First N lines - word + its distance in format word distance
# Last line - the average distance, rounded to two digits after the decimal point

target = int(input())

words_amount = int(input())
word_sum = 0
word_input = ""
word_diff = 0
avg_sum = 0

for i in range(words_amount):
    word_input = input()
    word_sum = 0
    for char in word_input:
        word_sum += ord(char) - 96
    word_diff = abs(word_sum - target)
    print(f"{word_input} {word_diff}")
    avg_sum += word_diff

avg_sum /= words_amount
print(f"{avg_sum:.2f}")