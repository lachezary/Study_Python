# Input
# Will always consists of one valid integer number - the number N.
# Output
# Should always consists of the numbers from 1 to N, which are not divisible by 3 or 7, separated by a whitespace.

num1 = int(input())

for i in range(1, num1+1):
    if i % 3 == 0 or i % 7 == 0:
        continue
    else:
        print(i, end=" ")
