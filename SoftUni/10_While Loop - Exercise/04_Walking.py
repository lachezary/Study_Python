
steps_target = 10000
steps_total = 0
status = ""

while steps_total < steps_target:
    steps = input()
    if steps.isdigit():
        steps_total += int(steps)
    elif steps == "Going home":
        status = "Going home"
        steps = int(input())
        steps_total += int(steps)
        break


steps_diff = abs(steps_total - steps_target)

if steps_total >= steps_target:
    print(f"Goal reached! Good job!")
    print(f"{steps_diff} steps over the goal!")
elif steps_total < steps_target:
    print(f"{steps_diff} more steps to reach goal.")
