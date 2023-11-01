


range_start = int(input())
range_end = int(input())
target = int(input())
first = 0
second = 0
third = 0
current_str = ""
current_num = 0

for i in range(range_start, range_end+1):
    current_str = str(i)
    first = current_str[0]
    second = current_str[1]
    third = current_str[2]
    current_num = int(first) + int(second) + int(third)
    if current_num == target:
        print(current_str)
    