num1 = int(input())
num2 = int(input())
operator = input()

result = 0
digit_type = "odd or even"


if operator == "+":
    result = num1 + num2
    if result % 2 == 0:
        digit_type = "even"
    else:
        digit_type = "odd"
    print(f"{num1} + {num2} = {result} - {digit_type}")
elif operator == "-":
    result = num1 - num2
    if result % 2 == 0:
        digit_type = "even"
    else:
        digit_type = "odd"
    print(f"{num1} - {num2} = {result} - {digit_type}")
elif operator == "*":
    result = num1 * num2
    if result % 2 == 0:
        digit_type = "even"
    else:
        digit_type = "odd"
    print(f"{num1} * {num2} = {result} - {digit_type}")
elif operator == "/":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else: 
        result = num1 / num2
        if result % 2 == 0:
            digit_type = "even"
        else:
            digit_type = "odd"
        print(f"{num1} / {num2} = {result:.2f}")
elif operator == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:       
        result = num1 % num2
        if result % 2 == 0:
            digit_type = "even"
        else:
            digit_type = "odd"
        print(f"{num1} % {num2} = {result}")
   
