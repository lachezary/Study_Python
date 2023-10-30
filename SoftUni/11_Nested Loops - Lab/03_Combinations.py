# Напишете програма, която изчислява колко решения
# в естествените числа (включително и нулата) има уравнението:
# x1 + x2 + x3 = n
# Числото n е цяло число и се въвежда от конзолата.

num = int(input())
solution_count = 0

for i1 in range(num+1):
    for i2 in range(num+1):
        for i3 in range(num+1):
            result = i1 + i2 + i3
            if result == num:
                solution_count += 1

print(solution_count)
