month_input = input()
days_stay = int(input())

studio_cost = 0
apartment_cost = 0

if month_input == "May" or month_input == "October":
    studio_cost = days_stay * 50
    apartment_cost = days_stay * 65
    if days_stay > 7 and days_stay <= 14:
        studio_cost = studio_cost * 0.95
    elif days_stay > 14:
        studio_cost = studio_cost * 0.7
        apartment_cost = apartment_cost * 0.9
elif month_input == "June" or month_input == "September":
    studio_cost = days_stay * 75.20
    apartment_cost = days_stay * 68.70
    if days_stay > 14:
        studio_cost = studio_cost * 0.8
        apartment_cost = apartment_cost * 0.9    
elif month_input == "July" or month_input == "August":
    studio_cost = days_stay * 76
    apartment_cost = days_stay * 77
    if days_stay > 14:
        apartment_cost = apartment_cost * 0.9   

print(f"Apartment: {apartment_cost:.2f} lv.")
print(f"Studio: {studio_cost:.2f} lv.")

