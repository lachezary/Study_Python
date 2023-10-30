# Write a program that finds the prime factors of a given non-prime number.
# List the factors in ascending order.

# 12 = 2 * 2 * 3
# 100 = 2 * 2 * 5 * 5
# Input
# On the first line you will receive one number - N
# Output
# Output each prime factor on a newline.
# Constraints
# 4 <= N <= 1000
# N is guaranteed to not be a prime


num = int(input())
prime = 2

for i in range(2, num+1):
    if num % prime == 0:
        print(prime)
        num /= prime
    else:
        prime += 1
