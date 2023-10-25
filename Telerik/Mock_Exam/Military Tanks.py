# Military scientists are training battle tanks
# using artificial intelligence. The first lesson
# is to teach them to move across the (x,y) - plane.
# They give them a sequence of moves and observe
# whether the tanks get to the correct (x, y) position
# on the field. This sequence is represented by string,
# and the character at position i represents the tank’s i-th move.

# There are several commands
# – R – moves right, L – moves left, U – moves up and D – moves down.

# To help the scientists, you have to write a program
# that collects the learning results of the tanks.


# RLDULLR

position = input()

count_l = position.count("L")
count_u = position.count("U")
count_d = position.count("D")
count_r = position.count("R")

count_d = count_d * -1
count_l = count_l * -1

vertical = count_d + count_u
horizontal = count_l + count_r

print(F"({horizontal}, {vertical})")
