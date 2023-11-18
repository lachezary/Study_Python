# За всеки ден се чете по едно число:
#  Добито злато за деня – реално число в интервала [0.00.. 1000.00]


# Изход:
# След приключване на копаенето на дадена локация се печата един ред според случая:
#  Ако средният добив злато за ден достига или 
# надвишава очаквания среден добив на ден злато:
# o "Good job! Average gold per day: {среден добив на ден за дадената локация}."
#  Ако средният добив злато за ден е под очаквания среден добив на ден злато:
# o "You need {злато, което не е достигнало за достигане на очакваният среден добив} gold."
# Резултатът да бъде форматиран до вторият знак след десетичният разделител.

locations = int(input())
average_income = 0
average_production = 0
working_days = 0

for _ in range(locations):
    average_production = 0
    average_income = float(input())
    working_days = int(input())
    for _ in range (working_days):
        production = float(input())
        average_production += production
    average_production /= working_days
    if float(average_income) <= float(average_production):
        print(f"Good job! Average gold per day: {average_production:.2f}.")
    else:
        average_production = average_income - average_production
        print(f"You need {average_production:.2f} gold.")




