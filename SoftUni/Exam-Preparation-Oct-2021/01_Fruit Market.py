# Мария решава да мине на диета и отива до близкия пазар,
# за да купи ягоди, банани, портокали и
# малини. На конзолата се въвежда цената на ягодите в лв./кг. и количеството на бананите,
# портокалите, малините и ягодите, които трябва да закупи. Да се напише програма, която
# пресмята колко пари са ѝ необходими за да плати сметката, като знаете, че:
# • цената на малините е на половина по-ниска от тази на ягодите;
# • цената на портокалите е с 40% по-ниска от цената на малините;
# • цената на бананите е с 80% по-ниска от цената на малините.
# Вход
# От конзолата се четат 5 реда:
# 1. Цена на ягодите в лева – реално число в интервала [0.00 … 10000.00]
# 2. Количество на бананите в килограми – реално число в интервала [0.00 … 1 0000.00]
# 3. Количество на портокалите в килограми – реално число в интервала [0.00 … 10000.00]
# 4. Количество на малините в килограми – реално число в интервала [0.00 … 10000.00]
# 5. Количество на ягодите в килограми – реално число в интервала [0.00 … 10000.00]
# Изход
# Да се отпечата на конзолата едно число:
# • парите, които са необходими на Мария.
# Резултатът да се форматира до вторта цифра след десетичната запетая.


strawberry_price = float(input())
bananas_kg = float(input())  # 80% less of berry
oranges_kg = float(input())  # 40% less than berry
berry_kg = float(input())  # price 50% less of strawberry
strawberry_kg = float(input())

berry_price = strawberry_price * 0.5

strawberry_cost = strawberry_price * strawberry_kg
berry_cost = berry_kg * berry_price
bananas_cost = bananas_kg * (berry_price * 0.2)
oranges_cost = oranges_kg * (berry_price * 0.6)

total_cost = strawberry_cost + berry_cost + oranges_cost + bananas_cost

print(f"{total_cost:.2f}")
