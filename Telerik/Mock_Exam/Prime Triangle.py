






input_num = int(input())

is_prime = True

for prime_tester in range (1, input_num+1):
    if input_num % prime_tester == 0:
        if prime_tester == 1 or prime_tester == input_num:
            continue
        else:
            is_prime = False

                
print("prime" if is_prime else "not prime")