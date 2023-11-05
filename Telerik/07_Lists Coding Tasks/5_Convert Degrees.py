







celsius_list = input().split(" ")
fahrenheit_list = []
fahrenheit = 0

for value in celsius_list:
    fahrenheit = (int(value) * 9/5) + 32
    fahrenheit_list.append(round(fahrenheit))
    print(fahrenheit_list[-1])
    