# Input
# On the first line, you will receive the number N.
# On each of the next N lines, you will receive a single real number.
# Output
# You output must always consist of exactly 4 lines -
# the minimal element on the first line, the maximal on the second,
# the sum on the third and the average on the fourth, in the following format:

lines_input = int(input())

min_num = 10000
max_num = -10000
sum = 0
avg = 0

for i in range(lines_input):
    digit_input = float(input())
    if digit_input < min_num:
        min_num = digit_input
    if digit_input > max_num:
        max_num = digit_input
    sum += digit_input


avg = sum / lines_input

print(f"min={min_num:.2f}")
print(f"max={max_num:.2f}")
print(f"sum={sum:.2f}")
print(f"avg={avg:.2f}")
