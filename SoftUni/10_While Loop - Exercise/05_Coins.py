change = float(input())
coins = 0

change = int(change * 100)
if change // 200 > 0:
    coins += change // 200
    change = change - ((change // 200) * 200)

if change // 100 > 0:
    coins += change // 100
    change = change - ((change // 100) * 100)

if change // 50 > 0:
    coins += (change // 50)
    change = change - ((change // 50) * 50)

if change // 20 > 0:
    coins += (change // 20)
    change = change - ((change // 20) * 20)
if change // 10 > 0:
    coins += (change // 10)
    change = change - ((change // 10) * 10)
if change // 5 > 0:
    coins += (change // 5)
    change = change - ((change // 5) * 5)
if change // 2 > 0:
    coins += (change // 2)
    change = change - ((change // 2) * 2)
if change // 1 > 0:
    coins += (change // 1)
    change = change - ((change // 1) * 1)

print(coins)
