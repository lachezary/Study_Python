
month = input()
hours_in_club = int(input())
group_size = int(input())
day_night = input()

price_per_hour = 0
total_price = 0



if month == "march" or month == "april" or month == "may":
    if day_night == "day":
        price_per_hour = 10.50
    elif day_night == "night":
        price_per_hour = 8.40
elif month == "june" or month == "july" or month == "august":
    if day_night == "day":
        price_per_hour = 12.60
    elif day_night == "night":
        price_per_hour = 10.20
        
if group_size >= 4:
    price_per_hour *= 0.9

if hours_in_club >=  5:
    price_per_hour *= 0.5

total_price = price_per_hour * group_size * hours_in_club

print(f"Price per person for one hour: {price_per_hour:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")