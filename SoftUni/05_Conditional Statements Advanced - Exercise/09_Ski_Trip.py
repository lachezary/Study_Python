days = int(input())
room_type = input()
rating_input = input()
vacation_cost = 0

days_stay = days - 1

if room_type == "room for one person":
    vacation_cost = days_stay * 18
elif room_type == "apartment":
    vacation_cost = days_stay * 25
    if days_stay < 10:
        vacation_cost = vacation_cost * 0.7
    elif days_stay > 10 and days_stay <=15:
        vacation_cost = vacation_cost * 0.65
    elif days_stay > 15:
        vacation_cost = vacation_cost * 0.5
elif room_type == "president apartment":
    vacation_cost = days_stay * 35
    if days_stay < 10:
        vacation_cost = vacation_cost * 0.9
    elif days_stay > 10 and days_stay <=15:
        vacation_cost = vacation_cost * 0.85
    elif days_stay > 15:
        vacation_cost = vacation_cost * 0.8

if rating_input == "positive":
    vacation_cost = vacation_cost * 1.25
elif rating_input == "negative":
    vacation_cost = vacation_cost * 0.9


print(f"{vacation_cost:.2f}")
