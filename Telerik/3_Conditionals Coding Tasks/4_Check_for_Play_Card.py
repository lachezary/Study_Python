# Classical play cards use the following signs to designate the card face: 
# 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K and A. 
# Write a program that enters a string and prints "yes" if it is a valid card sign or "no" otherwise.

# Input
# On the only line you will receive a single string.
# Output
# Output "yes" if the string is a card sign, otherwise print "no".
# Constraints
# String length will always be between 1 and 5
# Sample tests

card = input()

if card == "J":
    print("yes")
elif card == "J":
    print("yes")
elif card == "Q":
    print("yes")
elif card == "K":
    print("yes")
elif card == "A":
    print("yes")
elif int(card) >= 2 and int(card) <= 10:
    print("yes")
else:
    print("no")

