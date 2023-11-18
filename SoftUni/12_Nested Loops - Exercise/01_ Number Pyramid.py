num = int(input())
row = 1
start = 1

for i in range(1, num+1):
    for row in range(1, i+1):
        print(start, end=" ")
        start += 1
        if start > num:
            break
    print("")
    if start > num:
        break

