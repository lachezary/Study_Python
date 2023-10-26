# On the first line, you will receive N - the number of the values you must read
# On the next N lines you will receive numbers.
# Output
# On the only line of output, print the average with two digits after the decimal point.


lines_input = int(input())

total = 0
average = 0

for i in range(lines_input):
    num_input = float(input())
    total += num_input


average = total / lines_input
print(f"{average:.2f}")
