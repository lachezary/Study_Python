




numbers_list = input().split(",")

reversed_list = numbers_list.copy()
reversed_list.reverse()
equal_list = True

nums_to_compare = int(input())

front_number = 0
back_number = 0

for i in range (nums_to_compare):
    front_number = numbers_list[i]
    back_number = reversed_list[i]
    if numbers_list[i] != reversed_list[i]:
        equal_list = False
        break


if equal_list == False:
    print(f"false {front_number},{back_number}")
else:
    result = ','.join(map(str, numbers_list[:nums_to_compare]))
    print(f"true {result}")
