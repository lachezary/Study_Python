product_input = input()
city_input = input()
quantity_input = float(input())
product_cost = 0

if product_input == "coffee":
    if city_input == "Sofia":
        product_cost = quantity_input * 0.50
        print(product_cost)
    elif city_input == "Plovdiv":
        product_cost = quantity_input * 0.40
        print(product_cost)
    elif city_input == "Varna":
        product_cost = quantity_input * 0.45
        print(product_cost)
elif product_input == "water":
    if city_input == "Sofia":
        product_cost = quantity_input * 0.80
        print(product_cost)
    elif city_input == "Plovdiv":
        product_cost = quantity_input * 0.70
        print(product_cost)
    elif city_input == "Varna":
        product_cost = quantity_input * 0.70
        print(product_cost)
elif product_input == "beer":
    if city_input == "Sofia":
        product_cost = quantity_input * 1.20
        print(product_cost)
    elif city_input == "Plovdiv":
        product_cost = quantity_input * 1.15
        print(product_cost)
    elif city_input == "Varna":
        product_cost = quantity_input * 1.10
        print(product_cost)
elif product_input == "sweets":
    if city_input == "Sofia":
        product_cost = quantity_input * 1.45
        print(product_cost)
    elif city_input == "Plovdiv":
        product_cost = quantity_input * 1.30
        print(product_cost)
    elif city_input == "Varna":
        product_cost = quantity_input * 1.35
        print(product_cost)
elif product_input == "peanuts":
    if city_input == "Sofia":
        product_cost = quantity_input * 1.60
        print(product_cost)
    elif city_input == "Plovdiv":
        product_cost = quantity_input * 1.50
        print(product_cost)
    elif city_input == "Varna":
        product_cost = quantity_input * 1.55
        print(product_cost)