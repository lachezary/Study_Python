input_type = input()

if input_type == "integer":
    input_value = int(input())
    result = input_value + 1
    print(result)    
elif input_type == "real":
    input_value = float(input())
    result = input_value + 1
    print(f"{result:.2f}")
elif input_type == "text":
    input_value = input()
    result = str(input_value)
    print(f"{input_value}*")


