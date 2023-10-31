food_1 = ""
food_2 = ""
while food_1 != "END":
    food_1 = input()
    if food_2 == "":
        food_2 == food_1
    if food_1 == "END":
        break
    if len(food_1) >= len(food_2):
        result = food_1
    else:
        result = food_2
        
print(result)