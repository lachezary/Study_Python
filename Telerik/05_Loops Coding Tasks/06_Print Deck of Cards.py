# Input
# On the only line, you will receive the sign of the card to which you should print the cards in the deck.
# Output
# The output should follow the format defined in the sample tests below.
# Constraints
# The input character will always be a valid card sign.


# from curses.ascii import isdigit


card_target = input()


if card_target.isdigit():
    card_target = int(card_target)
    for i in range(2, card_target+1):
        print(f"{i} of spades, {i} of clubs, {i} of hearts, {i} of diamonds")
elif card_target == "J":
    for i in range(2, 11):
        print(f"{i} of spades, {i} of clubs, {i} of hearts, {i} of diamonds")
    print(f"J of spades, J of clubs, J of hearts, J of diamonds")
elif card_target == "Q":
    for i in range(2, 11):
        print(f"{i} of spades, {i} of clubs, {i} of hearts, {i} of diamonds")
    print(f"J of spades, J of clubs, J of hearts, J of diamonds")
    print(f"Q of spades, Q of clubs, Q of hearts, Q of diamonds")
elif card_target == "K":
    for i in range(2, 11):
        print(f"{i} of spades, {i} of clubs, {i} of hearts, {i} of diamonds")
    print(f"J of spades, J of clubs, J of hearts, J of diamonds")
    print(f"Q of spades, Q of clubs, Q of hearts, Q of diamonds")
    print(f"K of spades, K of clubs, K of hearts, K of diamonds")
elif card_target == "A":
    for i in range(2, 11):
        print(f"{i} of spades, {i} of clubs, {i} of hearts, {i} of diamonds")
    print(f"J of spades, J of clubs, J of hearts, J of diamonds")
    print(f"Q of spades, Q of clubs, Q of hearts, Q of diamonds")
    print(f"K of spades, K of clubs, K of hearts, K of diamonds")
    print(f"A of spades, A of clubs, A of hearts, A of diamonds")
