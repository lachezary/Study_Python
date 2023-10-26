num1 = int(input())
num2 = int(input())
result_evens = 0
result_ods = 0

for i in range(num1, num2+1):
    work_num = str(i)
    result_evens = int(work_num[0]) + int(work_num[2]) + int(work_num[4])
    result_ods = int(work_num[1]) + int(work_num[3]) + int(work_num[5])
    if result_evens == result_ods:
        print(work_num, end=" ")
