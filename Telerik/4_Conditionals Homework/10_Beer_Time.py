time_input = input()

try:
    hours = int(time_input[-8:-6])
    minutes = int(time_input[-5:-3])
    am_pm = time_input[-2:]

    if (am_pm == "PM" and hours >= 1 and minutes >= 0) and (am_pm == "PM" and hours <= 11 and minutes <= 59):
        print("beer time")
    elif (am_pm == "AM" and ((hours >= 0 and minutes >= 0) and (hours <= 2 and minutes <= 59))):
        print("beer time")
    elif am_pm == "PM" and hours == 12:
        print("non-beer time")
    elif (am_pm == "AM" and ((hours >= 3 and minutes >= 0) and (hours <= 11 and minutes <= 59))):
        print("non-beer time")
    else:
        print("invalid time")
except ValueError:
    print("invalid time")
