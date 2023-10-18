fruit_input = input()
day_input = input()
quantity_input = float(input())

work_days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend_days_list = ["Saturday", "Sunday"]

cost = 0

if fruit_input == "banana":
    if day_input in work_days_list:
        cost = quantity_input * 2.5
        print(f"{cost:.2f}")
    elif day_input in weekend_days_list:
        cost = quantity_input * 2.7
        print(f"{cost:.2f}")
    else:
        print("error")
elif fruit_input == "apple":
    if day_input in work_days_list:
        cost = quantity_input * 1.2
        print(f"{cost:.2f}")
    elif day_input in weekend_days_list:
        cost = quantity_input * 1.25
        print(f"{cost:.2f}")
    else:
        print("error")
elif fruit_input == "orange":
    if day_input in work_days_list:
        cost = quantity_input * 0.85
        print(f"{cost:.2f}")
    elif day_input in weekend_days_list:
        cost = quantity_input * 0.90
        print(f"{cost:.2f}")
    else:
        print("error")
elif fruit_input == "grapefruit":
    if day_input in work_days_list:
        cost = quantity_input * 1.45
        print(f"{cost:.2f}")
    elif day_input in weekend_days_list:
        cost = quantity_input * 1.60
        print(f"{cost:.2f}")
    else:
        print("error")
elif fruit_input == "grapefruit":
    if day_input in work_days_list:
        cost = quantity_input * 1.45
        print(f"{cost:.2f}")
    elif day_input in weekend_days_list:
        cost = quantity_input * 1.60
        print(f"{cost:.2f}")
    else:
        print("error")
elif fruit_input == "kiwi":
    if day_input in work_days_list:
        cost = quantity_input * 2.7
        print(f"{cost:.2f}")
    elif day_input in weekend_days_list:
        cost = quantity_input * 3.0
        print(f"{cost:.2f}")
    else:
        print("error")
elif fruit_input == "pineapple":
    if day_input in work_days_list:
        cost = quantity_input * 5.50
        print(f"{cost:.2f}")
    elif day_input in weekend_days_list:
        cost = quantity_input * 5.60
        print(f"{cost:.2f}")
    else:
        print("error")
elif fruit_input == "grapes":
    if day_input in work_days_list:
        cost = quantity_input * 3.85
        print(f"{cost:.2f}")
    elif day_input in weekend_days_list:
        cost = quantity_input * 4.2
        print(f"{cost:.2f}")
    else:
        print("error")
else:
    print("error")