

num1 = int(input())
power = 0


for i in range(num1+1):
    result = 2 ** power
    print(result)
    power += 2
    if power > num1:
        break
