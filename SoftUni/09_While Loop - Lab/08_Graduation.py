studen_name = input()
current_class = 1
average_score = 0
score = 0
failed = 0

while current_class <= 12:
    score = float(input())
    if score < 4:
        failed += 1
        if failed >= 2:
            break
        continue
    average_score += score
    current_class += 1


average_score /= 12

if failed < 2:
    print(f"{studen_name} graduated. Average grade: {average_score:.2f}")
else:
    print(f"{studen_name} has been excluded at {current_class} grade")
