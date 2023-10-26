free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

space_volume = free_space_width * free_space_height * free_space_length
moving_box = ""


while space_volume > 0:
    moving_box = input()
    if moving_box == "Done":
        break
    else:
        moving_box = int(moving_box)
        space_volume -= moving_box

if moving_box == "Done":
    print(f"{space_volume} Cubic meters left.")
else:
    space_volume = abs(space_volume)
    print(f"No more free space! You need {space_volume} Cubic meters more.")
