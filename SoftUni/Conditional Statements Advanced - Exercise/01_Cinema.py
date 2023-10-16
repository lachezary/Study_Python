screen_type = input()
rows = int(input())
columns = int(input())

premiere_price = 12.00
normal_price = 7.50
discounted_price = 5.00
income = 0

capacity = columns * rows

if screen_type == "Premiere":
    income = premiere_price * capacity
    print(f"{income:.2f} leva")
elif screen_type == "Normal":
    income = normal_price * capacity
    print(f"{income:.2f} leva")
elif screen_type == "Discount":
    income = discounted_price * capacity
    print(f"{income:.2f} leva")