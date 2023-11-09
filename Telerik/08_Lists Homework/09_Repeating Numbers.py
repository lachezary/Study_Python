input_ints = int(input())
num_list = []

for _ in range(input_ints):
    new_int = int(input())
    num_list.append(new_int)

max_count = 0
result = 0

for num in range(1, 11):
    count = num_list.count(num)
    if count > max_count:
        max_count = count
        result = num
    elif count == max_count and count != 0 and num < result:
        result = num

print(result)



