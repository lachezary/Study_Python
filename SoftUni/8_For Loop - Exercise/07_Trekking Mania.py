lines_of_groups = int(input())

mousala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for i in range(lines_of_groups):
    group_size = int(input())
    if group_size <= 5:
        mousala += group_size
    elif group_size <= 12:
        monblan += group_size
    elif group_size <= 25:
        kilimandjaro += group_size
    elif group_size <= 40:
        k2 += group_size
    elif group_size > 40:
        everest += group_size

total = mousala + monblan + kilimandjaro + k2 + everest

mousala = mousala / total
monblan = monblan / total
kilimandjaro = kilimandjaro / total
k2 = k2 / total
everest = everest / total

print(f"{mousala:.2%}")
print(f"{monblan:.2%}")
print(f"{kilimandjaro:.2%}")
print(f"{k2:.2%}")
print(f"{everest:.2%}")
