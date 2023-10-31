# Input
# The input consists of at least 2 lines
# The last line is always END
# Each different food is on a new line
# Output
# Print the food with the longest name. If two or more foods have equal length, print the last one.
# Constraints
# 1 <= lines of input <= 50 The last line will always be END

new_food = ""
result = ""

while new_food != "END":
    new_food = input()
    if new_food == "END":
        break
    if len(result) < 1:
        result = new_food
    elif len(new_food) >= len(result):
        result = new_food
        
        
print(result)