flowers_type = input()
flowers_pcs = int(input())
budget = float(input())

total = 0
change = 0


if flowers_type == "Roses":
    total = flowers_pcs * 5
    if flowers_pcs > 80:
        total = total * 0.9
elif flowers_type == "Dahlias":
    total = flowers_pcs * 3.8
    if flowers_pcs > 90:
        total = total * 0.85
elif flowers_type == "Tulips":
    total = flowers_pcs * 2.8
    if flowers_pcs > 80:
        total = total * 0.85
elif flowers_type == "Narcissus":
    total = flowers_pcs * 3
    if flowers_pcs < 120:
        total = total * 1.15
elif flowers_type == "Gladiolus":
    total = flowers_pcs * 2.5
    if flowers_pcs < 80:
        total = total * 1.2

change = abs(budget - total)

if budget >= total:
    print(f"Hey, you have a great garden with {flowers_pcs} {flowers_type} and {change:.2f} leva left.")
else:
    print(f"Not enough money, you need {change:.2f} leva more.")