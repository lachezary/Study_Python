nums = int(input())
first_value = int(input())

min_number = first_value
max_number = first_value

for i in range(1, nums):
    test_num = int(input())
    if test_num < min_number:
        min_number = test_num
    elif test_num > max_number:
        max_number = test_num

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
