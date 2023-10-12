week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

user_input = int(input())
if user_input >= 1 and user_input <= 7:
    print(week_days[user_input-1])
else:
    print("Error")
