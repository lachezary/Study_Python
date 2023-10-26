# •	На всеки четен етаж има само офиси;
# •	На всеки нечетен етаж има само апартаменти;
# •	Всеки апартамент се означава по следния начин :
# А{номер на етажа}{номер на апартамента}, номерата на апартаментите започват от 0;
# •	Всеки офис се означава по следния начин :
# О{номер на етажа}{номер на офиса}, номерата на офисите също започват от 0;
# •	На последният етаж винаги има апартаменти
# и те са по-големи от останалите, затова пред номера им пише 'L', вместо 'А'.
# Ако има само един етаж, то има само големи апартаменти!


floors_total = int(input())
rooms_per_floor = int(input())
current_floor = 1
large_counter = 0

for floors in range(floors_total, 0, -1):
    for rooms in range(0, rooms_per_floor):
        if large_counter < rooms_per_floor:
            print(f"L{floors}{rooms}", end=' ')
            large_counter += 1
        elif floors % 2 != 0:
            print(f"A{floors}{rooms}", end=' ')
        elif floors % 2 == 0:
            print(f"O{floors}{rooms}", end=' ')
    print("")
