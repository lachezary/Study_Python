from sre_compile import isstring


test_input = input()

try:
    if test_input.isdecimal():
        print("decimal")
    else:
        print(f"{test_input[0]}")

except IndexError or ValueError:
    print("Error")
