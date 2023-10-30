# Use the coins of 1 lev, 50, 20, 10, 5, 2 and 1 stotinki.

# Input
# On the first line, you will receive the price in leva.
# On the second line, you will receive how much the customer has paid in leva.
# Output
# There is a variable amount of output lines.
# Print each required denomination on a new line, ordered from highest to lowest.


price = float(input())
paid = float(input())

price *= 100
paid *= 100
change = paid - price
coins = 0

if change // 100 != 0:
    coins = change // 100
    print(f"{coins:.0f} x 1 lev")
    change = change - (coins * 100)
if change // 50 != 0:
    coins = change // 50
    print(f"{coins:.0f} x 50 stotinki")
    change = change - (coins * 50)
if change // 20 != 0:
    coins = change // 20
    print(f"{coins:.0f} x 20 stotinki")
    change = change - (coins * 20)
if change // 10 != 0:
    coins = change // 10
    print(f"{coins:.0f} x 10 stotinki")
    change = change - (coins * 10)
if change // 5 != 0:
    coins = change // 5
    print(f"{coins:.0f} x 5 stotinki")
    change = change - (coins * 5)
if change // 2 != 0:
    coins = change // 2
    print(f"{coins:.0f} x 2 stotinki")
    change = change - (coins * 2)
if change // 1 != 0:
    coins = change // 1
    print(f"{coins:.0f} x 1 stotinka")
    change = change - (coins * 1)


# 1 x 50 stotinki
# 1 x 20 stotinki
# 1 x 10 stotinki
# 1 x 5 stotinki
# 1 x 2 stotinki
# 1 x 1 stotinka
