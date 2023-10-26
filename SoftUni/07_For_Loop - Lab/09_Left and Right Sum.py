amount_num = int(input())

sum1 = 0
sum2 = 0


for i in range(amount_num):
    num1 = int(input())
    sum1 += num1

for i in range(amount_num):
    num2 = int(input())
    sum2 += num2

if sum1 == sum2:
    print(f"Yes, sum = {sum1}")
else:
    sums = abs(sum1 - sum2)
    print(f"No, diff = {sums}")
