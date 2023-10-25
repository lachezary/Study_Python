num = int(input())

for i in range(1, num + 1):
    for prime in range(2, i):
        if i % prime == 0:
            print(0, end="")
            break
    else:
        print(1, end="")
    if i < num:
        print(" ", end="")
print()
