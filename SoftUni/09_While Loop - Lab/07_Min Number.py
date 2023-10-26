input_data = ""
min_num = float("inf")

while input_data != "Stop":
    input_data = input()
    try:
        input_data = float(input_data)
        if input_data < min_num:
            min_num = input_data
    except ValueError:
        pass

min_num = int(min_num)
print(min_num)
