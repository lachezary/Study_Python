working_days = ["Monday","Tuesday","Wednesday", "Thursday", "Friday"]
weekend_days = ["Saturday","Sunday"]

day_input = input()

if day_input in working_days:
    print("Working day")
elif day_input in weekend_days:
    print("Weekend")
else:
    print("Error")
