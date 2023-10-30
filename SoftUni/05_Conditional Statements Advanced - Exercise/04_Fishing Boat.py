budget = float(input())
season = input()
fishermen_quantity = int(input())

boat_rent = 0
change = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Summer":
    boat_rent = 4200
elif season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if fishermen_quantity <= 6:
    boat_rent = boat_rent * 0.9
elif fishermen_quantity >= 7 and fishermen_quantity <= 11:
    boat_rent = boat_rent * 0.85
elif fishermen_quantity > 11:
    boat_rent = boat_rent * 0.75

if season != "Autumn":
    if fishermen_quantity % 2 == 0:
        boat_rent = boat_rent * 0.95

change = abs(budget - boat_rent)

if budget >= boat_rent:
    print(f"Yes! You have {change:.2f} leva left.")
else:
    print(f"Not enough money! You need {change:.2f} leva.")

