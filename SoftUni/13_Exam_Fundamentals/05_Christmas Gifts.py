#  Всички до 16 (вкл.) години се считат за деца и ще получат играчка
#  Всички над 16 години се считат за възрастни и ще получат коледен пуловер
#  Цената на всяка играчка е 5 лв., а цената на един пуловер е 15 лв.
# Напишете програма, която пресмята колко души от семейството на Иван са до 16 (вкл.) години и колко са
# над тази възраст, също и колко пари ще струват подаръците на децата и възрастните.
# 
# Вход:
# От конзолата се четат поредица от редове до получаване на команда "Christmas":
#  Годините на всеки член от семейството - цяло число в интервала [1 … 130]
# Изход:
# Да се отпечатат на конзолата четири реда:
#  "Number of adults: {брой хора над 16 години}"
#  "Number of kids: {брой хора до 16 (вкл.) години}"
#  "Money for toys: {сумата за всички играчки}"
#  "Money for sweaters: {сума за всички пуловери}"
kids = 0
adults = 0
new_input = ""

while new_input != "Christmas":
    new_input = input()
    if new_input == "Christmas":
        break
    elif int(new_input) <= 16:
        kids += 1
    elif int(new_input) > 16:
        adults += 1
        

toy_price = 5
sweater_price = 15

toys_cost = kids * toy_price
sweater_cost = adults * sweater_price

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {toys_cost}")
print(f"Money for sweaters: {sweater_cost}")