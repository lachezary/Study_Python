
number = input()

number = number.replace(".", "")
number = number.replace("-", "")

length = len(number)
total = 0

while length >= 2:
    total = 0
    for i in range(length):
        digit = int(number[i])
        total += digit
    number = str(total)
    length = len(number)
    if total < 10:
        break

print(total)
