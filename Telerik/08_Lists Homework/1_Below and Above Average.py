# Input
# On the only line of input, you will receive the numbers, separated by a comma.
# Output
# On the first line, print the average, with two digits after the decimal separator.
# On the second line, print all the numbers bellow the average
# On the third line, print all the numbers above the average

num_list = input().split(",")
list_avg = 0
below_avg_num = []
above_avg_num = []

numbers = num_list.copy()

for i in num_list:
    list_avg = list_avg + int(i)

list_avg = list_avg / len(num_list)

for num in num_list:
    if int(num) < list_avg:
        below_avg_num.append(num)
    elif int(num) > list_avg:
        above_avg_num.append(num)

print(f"avg: {list_avg:.2f}")
print("below: ", end="")
print(",".join(map(str, below_avg_num)))
print("above: ", end="")
print(",".join(map(str, above_avg_num)))

