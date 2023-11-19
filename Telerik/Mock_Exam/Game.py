num = input()
total = 0

num1 = int(num[0])
num2 = int(num[1])
num3 = int(num[2])

if num.count("1") >= 2 or num.count("0") >= 2:
    total = num1 + num2 + num3
elif num.count("1") == 1 and num.count("0") == 1:
    total = num1 + num2 + num3
    
elif num.count("1") == 1 or num.count("0") == 1:
    if num1 <= 1:
        total = num2 * num3 + num1
    elif num2 <= 1:
        total = num3 * num1 + num2
    elif num3 <= 1:
        total = num2 * num1 + num3
else:
    total = num1 * num2 * num3
    
    
    
print(total)
