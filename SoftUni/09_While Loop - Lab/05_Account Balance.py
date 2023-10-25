total = 0
input_data = ""

while input_data != "NoMoreMoney":
    input_data = input()
    try:
        input_data = float(input_data)
        if input_data <= 0:
            print("Invalid operation!")
            break
        else:
            print(f"Increase: {input_data:.2f}")
            total += input_data
    except ValueError:
        if input_data == "NoMoreMoney":
            break

print(f"Total: {total:.2f}")
