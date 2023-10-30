# Sum Positive
# Write a program that reads a positive integer (n) 
# You must print the sum of all integers from 1 to n.

# Hint
# You could use the formula sum = n*(n+1)/2
# Input
# On the first line you will receive a number (n)
# Output
# You should print the sum of the integers from 1 to n

num1 = int(input())

sum = num1*(num1+1)/2
sum = int(sum)
print(sum)
