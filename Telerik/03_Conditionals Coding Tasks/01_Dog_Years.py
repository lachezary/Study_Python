# Most people believe that 1 human year (HY) equals 7 dog years (DY), 
# however, dogs reach adulthood in approximately 2 human years.

# So it's better to count the first two HY as 10 DY each and then count 
# the remaining HY as 4 DY each.

# Write a program that correctly converts human years (HY) to dog years (DY). 
# You may need some form of conditional logic.

# Input
# On the first line, you will receive HY - the number of human years.
# Output
# On the only line of output, print DY - the number of dog years.
# Constraints
# 1 <= HY <= 15


human_years = int(input())
dog_years = 0

if human_years <= 2:
    dog_years = human_years * 10
    print(dog_years)
else:
    dog_years = ((human_years - 2) * 4) + 20
    print(dog_years)