start_range = int(input())
end_range = int(input())
magic_num = int(input())

first_num = 0
second_num = 0
result = 0
combination_nr = 0

found = False

for first_num in range(start_range, end_range+1):
    for second_num in range(start_range, end_range+1):
        combination_nr += 1
        result = first_num + second_num
        if result == magic_num:
            found = True
            break
        result = 0
    if found:
        break


if found:
    print(
        f"Combination N:{combination_nr} ({first_num} + {second_num} = {result})")
else:
    print(f"{combination_nr} combinations - neither equals {magic_num}")
