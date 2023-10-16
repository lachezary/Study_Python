exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())


exam_time = exam_hours * 60 + exam_minutes
arrival_time =  arrival_hours * 60 + arrival_minutes

difference_time = abs(arrival_time - exam_time)
difference_hours = difference_time // 60
difference_minutes = difference_time % 60
# late_hours = arrival_hours - exam_hours
# late_minutes = arrival_minutes - exam_minutes



if arrival_time > exam_time:
    print("Late")
    if (arrival_time - 59) > exam_time:
        print(f"{difference_hours}:{difference_minutes:02} hours after the start")
    else:
        print(f"{difference_minutes} minutes after the start")
elif exam_time == arrival_time:
    print("On time")
elif (exam_time - arrival_time <= 30):
    print("On time")
    print(f"{difference_minutes} minutes before the start")
elif (exam_time - arrival_time <= 30):
    print("Early")
    print(f"{difference_minutes} minutes before the start")
elif (exam_time - arrival_time >= 30):
    print("Early")
    print(f"{difference_hours}:{difference_minutes:02} hours before the start")



     
