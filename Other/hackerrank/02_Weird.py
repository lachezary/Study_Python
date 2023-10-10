# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

num = int(input())

if num % 2 != 0:
    print("Weird")
elif num % 2 == 0:
    if num >=2 and num <=5:
        print("Not Weird")
    elif num >=6 and num <=20:
        print("Weird")
    elif num > 20:
                print("Not Weird")
