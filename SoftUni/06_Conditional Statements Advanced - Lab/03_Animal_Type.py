reptile_list = ["crocodile", "snake", "tortoise"] 
mammal_list = ["dog"]

user_input = input()

if user_input in reptile_list:
    print("reptile")
elif user_input in mammal_list:
    print("mammal")
else:
    print("unknown")
