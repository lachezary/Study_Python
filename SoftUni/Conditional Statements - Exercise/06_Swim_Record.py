world_record = float(input())
distance = float(input())
speed = float(input())


result = speed * distance

intervals = distance // 15
delay = intervals * 12.5

result = result + delay



if result < world_record:
    print(f"Yes, he succeeded! The new world record is {result:.2f} seconds.")
else:
    result = result - world_record
    print(f"No, he failed! He was {result:.2f} seconds slower.")
