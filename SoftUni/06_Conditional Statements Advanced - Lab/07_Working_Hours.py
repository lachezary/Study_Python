work_hours = [10, 11, 12, 13, 14, 15, 16, 17, 18]
work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

hour_input = int(input())
day_input = input()

if hour_input in work_hours and day_input in work_days:
    print("open")
else:
    print("closed")