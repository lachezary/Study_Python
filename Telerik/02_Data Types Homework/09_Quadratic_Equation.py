# Quadratic Equation
# Write a program that reads the coefficients 
# a, b and c of a quadratic equation ax2 + bx + c = 0 
# and solves it (prints its real roots x1 = (-b - sqrt(D)) / 2a, x2 = (-b + sqrt(D)) / 2a). 
# Assume there always will be one or two real roots (D = b2 - 4ac >= 0).

# Input
# Read from the standard input

# On 3 separate lines, exactly 3 numbers, which are the coefficients.
# Output
# Print on two separate lines the roots. (look at the sample tests)
# Print it to the first integer after the decimal point.



# ax2 + bx + c = 0 
# x1 = (-b - sqrt(D)) / 2a
# x2 = (-b + sqrt(D)) / 2a)
# D = b2 - 4ac >= 0


a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4 * a * c
x1 = (-b - (d ** 0.5)) / (2 * a)
x2 = (-b + (d ** 0.5)) / (2 * a)

print(f"x1={x1:.1f}")
print(f"x2={x2:.1f}")


