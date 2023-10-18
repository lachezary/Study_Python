product_input = input()

fruit_list = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetable_list = ["tomato", "cucumber", "pepper", "carrot"]

if product_input in fruit_list:
    print("fruit")
elif product_input in vegetable_list:
    print("vegetable")
else:
    print("unknown")
