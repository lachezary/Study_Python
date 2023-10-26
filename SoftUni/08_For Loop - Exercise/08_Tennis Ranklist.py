tournaments = int(input())
starting_points = int(input())

final_points = 0
average_points = 0
tournaments_win = 0


for i in range(tournaments):
    stage = input()
    if stage == "W":
        tournaments_win += 1
        final_points += 2000
    elif stage == "F":
        final_points += 1200
    elif stage == "SF":
        final_points += 720

average_points = int(final_points // tournaments)
tournaments_win = tournaments_win / tournaments
final_points += starting_points

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{tournaments_win:.2%}")
