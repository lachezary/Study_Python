savings = float(0)
travel_destination = ""
cost = float(0)
total_savings = float(0)


while travel_destination != "End":
    travel_destination = input()
    if travel_destination == "End":
        break
    cost = float(input())
    while total_savings < cost:
        savings = input()
        savings = float(savings)
        total_savings += float(savings)
        if total_savings >= cost:
            print(f"Going to {travel_destination}!")
            total_savings -= cost
            break
