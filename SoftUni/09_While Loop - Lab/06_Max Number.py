input_data = ""
big_num = float("-inf")

while input_data != "Stop":
    input_data = input()
    try:
        input_data = float(input_data)
        if input_data > big_num:
            big_num = input_data
    except ValueError:
        pass

big_num = int(big_num)
print(big_num)
