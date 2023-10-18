degrees = int(input())
daytime = input()

if degrees >= 10 and degrees <= 18:
    if daytime == "Morning":
        print(f"It's {degrees} degrees, get your Sweatshirt and Sneakers.")
    elif daytime == "Afternoon":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif daytime == "Evening":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
elif degrees > 18 and degrees <= 24:
    if daytime == "Morning":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif daytime == "Afternoon":
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
    elif daytime == "Evening":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
elif degrees > 24:
    if daytime == "Morning":
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
    elif daytime == "Afternoon":
        print(f"It's {degrees} degrees, get your Swim Suit and Barefoot.")
    elif daytime == "Evening":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")