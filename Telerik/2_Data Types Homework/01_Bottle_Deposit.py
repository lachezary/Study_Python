# # <!-- Bottle Deposit
# # When you buy something to drink you make a deposit for the bottle. 
# Each bottle has a different deposit. Half liter bottles have $0.1 
# deposit and the one liter bottles have $0.25 deposit. Calculate the 
# sum which you will make when returning the bottles. You must print 
# two digits after the decimal point.

# Input
# On the first line you will receive the number of 0.5L bottles.
# On the second line you will receive the number of 1L bottles.
# Output
# You should print the total sum you will earn. -->



half_liter_bottles = int(input())
liter_bottles = int(input())


half_liter = 0.1
liter = 0.25
sum = 0

half_liter = half_liter * half_liter_bottles
liter_bottles = liter_bottles * liter

sum = half_liter + liter_bottles
print(f"{sum:.2f}")