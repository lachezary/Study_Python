num1 = float(input())
num2 = float(input())
num3 = float(input())

result = num1 * num2 * num3

if result < 0:
    print("-")
elif result == 0:
    print("0")
else:
    print("+")