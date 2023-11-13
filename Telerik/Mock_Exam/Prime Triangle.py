






input_num = int(input())

is_prime = True
for prime_numbers in range (1, input_num+1):
    for prime_tester in range (1, prime_numbers+1):
        if prime_numbers % prime_tester == 0:
            if prime_tester == 1 or prime_tester == prime_numbers:
                print(prime_numbers)
                continue
            else:
                is_prime = False
                break