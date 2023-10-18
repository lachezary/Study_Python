# Write a program that reads days, hours, minutes and seconds from the standard input. 
# Display the total amount of seconds.

# Input
# First line - d - days
# Second line - h - hours
# Third line - m - minutes
# Fourth line - s - seconds
# Output
# On the only line of output, print the total amount of seconds
# Constraints
# 0 <= d, h, m, s <= 1000


days = int(input())
hours = int(input())
minutes = int(input())
seconds = int(input())

hours = (days*24) + hours
minutes = (hours*60) + minutes
seconds = (minutes*60) + seconds

print(seconds)

