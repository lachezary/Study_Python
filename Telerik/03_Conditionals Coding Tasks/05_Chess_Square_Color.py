label = input()
rank = int(input())


if label == "a" or label == "c" or label == "e" or label == "g":
    if rank % 2 == 0:
        print("light")
    elif rank % 2 != 0:
        print("dark")
elif label == "b" or label == "d" or label == "f" or label == "h":
    if rank % 2 == 0:
        print("dark")
    elif rank % 2 != 0:
        print("light")
