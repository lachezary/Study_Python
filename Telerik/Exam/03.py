import math


colleagues = int(input())
vineyard_length = float(input())
vineyard_quality = list(input())

#needed
wine_glasses_needed = colleagues * 2
rakia_glasses_needed = colleagues 

wine_bottles_needed = math.ceil(wine_glasses_needed / 5)
rakia_bottles_needed = math.ceil(rakia_glasses_needed / 14 )

if wine_glasses_needed > 0 and wine_bottles_needed == 0:
    wine_bottles_needed = 1
if rakia_glasses_needed > 0 and rakia_bottles_needed == 0:
    rakia_bottles_needed = 1



#produced
perfect_vines_kg = vineyard_quality.count("X") * 7
average_vines_kg = vineyard_quality.count("x") * 7

wine_bottles_produced = perfect_vines_kg 
rakia_bottles_produced = average_vines_kg // 5

wine_glasses_produced = wine_bottles_produced * 5
rakia_glasses_produced = rakia_bottles_produced * 14


#party
wine_bottles_remaining = abs(wine_bottles_produced - wine_bottles_needed)
rakia_bottles_remaining =  abs(rakia_bottles_produced - rakia_bottles_needed)



if wine_bottles_needed < wine_bottles_produced and rakia_bottles_needed < rakia_bottles_produced:
    print(f"Yes! {wine_bottles_remaining} bottles of wine and {rakia_bottles_remaining} bottles of rakia remaining for the next party!")
else:
    if wine_bottles_needed <= wine_bottles_produced:
        wine_bottles_remaining = 0
    if rakia_bottles_needed <= rakia_bottles_produced:
        rakia_bottles_remaining = 0
    print(f"No! {wine_bottles_remaining} more bottles of wine and {rakia_bottles_remaining} more bottles of rakia required!")
