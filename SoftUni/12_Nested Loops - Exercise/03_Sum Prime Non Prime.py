
input_data = ""
primes = 0
nonprimes = 0

while input_data != "stop":
    input_data = input()
    if input_data == "stop":
        break
    input_data = int(input_data)
    if input_data < 0:
        print("Number is negative.")
        continue

    is_prime = True
    if input_data <= 1:
        is_prime = False
    for i in range(2, int(input_data**0.5) + 1):
        if input_data % i == 0:
            is_prime = False

    if is_prime:
        primes += input_data
    else:
        nonprimes += input_data

print(f"Sum of all prime numbers is: {primes}")
print(f"Sum of all non prime numbers is: {nonprimes}")
