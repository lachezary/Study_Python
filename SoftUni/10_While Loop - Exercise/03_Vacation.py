travel_cost = float(input())
current_money = float(input())

spending_days = 0
saving_days = 0
all_days = 0

action = ""

while current_money < travel_cost:
    action = input()
    money = float(input())
    all_days += 1
    if action == "spend":
        current_money -= money
        spending_days += 1
        if current_money < 0:
            current_money = 0
    elif action == "save":
        current_money += money
        saving_days += 1
        spending_days = 0
    if spending_days >= 5:
        break

if spending_days >= 5:
    print("You can't save the money.")
    print(f"{all_days}")
elif current_money >= travel_cost:
    print(f"You saved the money for {all_days} days.")
