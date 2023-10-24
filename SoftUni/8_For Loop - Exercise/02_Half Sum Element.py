# Да се напише програма, която чете n-на брой цели числа, въведени от
# потребителя,и проверява дали сред тях съществува число, което е равно на
# сумата на всички останали.
# •	Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
# •	Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата
# между най-големия елемент и сумата на останалите (по абсолютна стойност)


nums = int(input())

biggest = 0
sum = 0

for i in range(nums):
    num_input = int(input())
    if num_input > biggest:
        biggest = num_input
    sum += num_input


sum -= biggest
diff = abs(biggest - sum)


if sum == biggest:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    print(f"Diff = {diff}")
