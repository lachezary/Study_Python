num = int(input())
old_num = -100000000
result = ""
equal = "="
smaller = ">"
bigger = "<"
for i in range(num):
    new_num = int(input())
    if i == 0:
        old_num = new_num
        result = new_num
    elif new_num > old_num:
        result = str(result) + str(bigger) + str(new_num)
        old_num = new_num
    elif new_num < old_num:
        result = str(result) + str(smaller) + str(new_num)
        old_num = new_num
    elif new_num == old_num:
        result = str(result) + str(equal) + str(new_num)
        old_num = new_num

print(result)