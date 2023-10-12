age_input = float(input())
gender_input = input()

if age_input >= 16:
    if gender_input == "f":
        print("Ms.")
    elif gender_input == "m":
        print("Mr.")
elif age_input < 16:
    if gender_input == "f":
        print("Miss")
    elif gender_input == "m":
        print("Master")

