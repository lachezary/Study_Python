# Input
# On the first line, you will receive the number N
# On each of the next N lines, you will receive a number 
# or word
# If the input is a word it won't contain any digits!
# Output
# If there is a number after a word we print the concatenated 
# words so far
# If there is a word after a number we print the sum so far

input_lines = int(input())

words_sum = ""
nums_sum = 0
num_count = 0
word_count = 0

for i in range (input_lines):
    new_input = input()
    if new_input[-1].isdigit():
        if word_count > 0:
            print(words_sum)
            words_sum = ""
            word_count = 0
    elif not(new_input[-1].isdigit()):
        if num_count > 0:
            print(nums_sum)
            nums_sum = 0
            num_count = 0
            
    if new_input[-1].isdigit():
        new_input = int(new_input)
        nums_sum += new_input
        num_count += 1
    else:
        if words_sum == "":
            words_sum = new_input
            word_count += 1
        else:
            words_sum = words_sum + "-" + new_input
            word_count += 1

if num_count == 0:
    print(words_sum)
elif word_count == 0:
    print(nums_sum)
