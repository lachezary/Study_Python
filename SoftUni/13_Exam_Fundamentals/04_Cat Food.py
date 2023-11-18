
# храната им за един ден, ако 1 кг храна = 12.45 лева.

# • Ако котката изяжда от 100 (вкл.) до 200 грама, 
# то тя попада в група 1: малки котки.
# • Ако котката изяжда от 200 (вкл.) до 300 грама, 
# то тя попада в група 2: големи котки.
# • Ако котката изяжда от 300 (вкл.) до 400 грама, 
# то тя попада в група 3: огромни котки.


cats_amount = int(input())

small_cats = 0
large_cats = 0
huge_cats = 0

total_food = 0 
food_price = 12.45


for _ in range(cats_amount):
    cat_food = float(input())
    if cat_food >= 100 and cat_food < 200:
        small_cats += 1
        total_food += cat_food
    elif cat_food >= 200 and cat_food < 300:
        large_cats += 1
        total_food += cat_food
    elif cat_food >= 300 and cat_food < 400:
        huge_cats += 1
        total_food += cat_food

total_food /= 1000
food_price *= total_food

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {large_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {food_price:.2f} lv.")



