

lily_age = int(input())
washing_machine_cost = float(input())
single_toy_price = float(input())

toys_count = 0
money_for_bd = 10
money_from_bd = 0
brother_took = 1

for i in range(1, lily_age+1):
    if i % 2 != 0:
        toys_count += 1
    elif i % 2 == 0:
        money_from_bd += money_for_bd
        money_for_bd += 10
        money_from_bd -= brother_took


toys_money = toys_count * single_toy_price
total = toys_money + money_from_bd


result = abs(washing_machine_cost - total)

if total >= washing_machine_cost:
    print(f"Yes! {result:.2f}")
else:
    print(f"No! {result:.2f}")
