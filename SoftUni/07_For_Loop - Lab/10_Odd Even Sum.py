num1 = int(input())
odd_sum = 0
even_sum = 0


for i in range(num1):
    nums = int(input())
    if i % 2 == 0:
        even_sum += nums
    else:
        odd_sum += nums


if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    difference = abs(odd_sum - even_sum)
    print(f"Diff = {difference}")
