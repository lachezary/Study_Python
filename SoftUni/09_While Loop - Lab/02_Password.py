user_name = input()
password = input()

data = ""

while data != password:
    data = input()

print(f"Welcome {user_name}!")
