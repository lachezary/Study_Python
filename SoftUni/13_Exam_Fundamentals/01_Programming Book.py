# 899 pages 2 covers

page_price = float(input())
cover_price = float(input())
discount_percentage = int(input())
designer_payment = float(input())
team_payment_percentage = int(input())


money = (page_price * 899) + (cover_price * 2)
money = money - (money  * (discount_percentage / 100))
money += designer_payment
money = money - (money  * (team_payment_percentage / 100))

print(f"Avtonom should pay {money:.2f} BGN.")