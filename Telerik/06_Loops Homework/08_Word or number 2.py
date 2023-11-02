# Input
# On the first line, you will receive the number N
# On each of the next N lines, you will receive a number or word
# If the input is a word it won't contain any digits!
# Output
# On the first line there are all words concatenated with - between them or 
# "no words" if there were no words in the input.
# On the second line is the sum of all the numbers or "0" if there were no numbers.


input_lines = int(input())

new_input = ""
sum_words = ""
sum_nums = 0
count = 0

for i in range (input_lines):
    new_input = input()
    if new_input.isdigit():
        new_input = int(new_input)
        sum_nums += new_input
    else:
        if count == 0:
            sum_words = new_input
            count += 1
        else:
            sum_words = sum_words + "-" + new_input

if sum_words == "":
    print("no words")
else:
    print(sum_words)
    
if sum_nums == 0:
    print("0")
else:
    print(sum_nums)