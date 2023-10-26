cake_width = int(input())
cake_length = int(input())

cake_pcs = cake_width * cake_length
cake_guests = ""

while cake_pcs >= 0:
    cake_guests = input()
    if cake_guests == "STOP":
        break
    cake_guests = int(cake_guests)
    cake_pcs -= cake_guests


if cake_guests == "STOP":
    print(f"{cake_pcs} pieces are left.")
else:
    cake_pcs = abs(cake_pcs)
    print(f"No more cake left! You need {cake_pcs} pieces more.")
