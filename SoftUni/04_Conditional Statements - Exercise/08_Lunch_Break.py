import math

tvshow_name = input()
series_length = int(input())
rest_length = int(input())

lunch = rest_length / 8
relax = rest_length / 4

free_time = rest_length - lunch - relax

if series_length <= free_time:
    left_time = math.ceil(free_time - series_length)
    print(f"You have enough time to watch {tvshow_name} and left with {left_time} minutes free time.")
else:
    left_time = math.ceil(series_length - free_time)
    print(f"You don't have enough time to watch {tvshow_name}, you need {left_time} more minutes.")