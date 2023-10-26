num = int(input())
special_num = 0
for i in range(1111, 10000):
    test_num = str(i)
    special_num1 = int(test_num[0])
    special_num2 = int(test_num[1])
    special_num3 = int(test_num[2])
    special_num4 = int(test_num[3])
    if special_num1 == 0 or special_num2 == 0 or special_num3 == 0 or special_num4 == 0:
        continue
    if num % special_num1 == 0 and num % special_num2 == 0 and num % special_num3 == 0 and num % special_num4 == 0:
        special_num = i
        print(i, end=" ")
