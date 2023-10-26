budget = float(input())
season = input()

holiday_price = 0

if budget <= 100:
    if season == "summer":
        holiday_price = budget * 0.3
        print(f"Somewhere in Bulgaria\nCamp - {holiday_price:.2f}")
    elif season == "winter":
        holiday_price = budget * 0.7
        print(f"Somewhere in Bulgaria\nHotel - {holiday_price:.2f}")
elif budget <= 1000:
    if season == "summer":
        holiday_price = budget * 0.4
        print(f"Somewhere in Balkans\nCamp - {holiday_price:.2f}")
    elif season == "winter":
        holiday_price = budget * 0.8
        print(f"Somewhere in Balkans\nHotel - {holiday_price:.2f}")
elif budget > 1000:
        holiday_price = budget * 0.9
        print(f"Somewhere in Europe\nHotel - {holiday_price:.2f}")