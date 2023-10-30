actor_name = input()
academy_points = float(input())
jury_ppl = int(input())
jury_member_points = 0
jury_name_length = 0
total_points = academy_points

for i in range(jury_ppl):
    jury_name = input()
    points = float(input())
    jury_name_length = len(jury_name)
    jury_member_points = (jury_name_length * points) / 2
    total_points += jury_member_points
    if total_points > 1250.5:
        break


not_enough_points = abs(1250.5 - total_points)

if total_points > 1250.5:
    print(
        f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {not_enough_points:.1f} more!")
