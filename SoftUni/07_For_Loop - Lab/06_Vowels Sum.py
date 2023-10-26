string_input = input()

letter_a = int(1)
letter_e = int(2)
letter_i = int(3)
letter_o = int(4)
letter_u = int(5)

sum = 0

letter_a = letter_a * string_input.count("a")
letter_e = letter_e * string_input.count("e")
letter_i = letter_i * string_input.count("i")
letter_o = letter_o * string_input.count("o")
letter_u = letter_u * string_input.count("u")


if "a" in string_input:
    sum += letter_a
if "e" in string_input:
    sum += letter_e
if "i" in string_input:
    sum += letter_i
if "o" in string_input:
    sum += letter_o
if "u" in string_input:
    sum += letter_u

print(sum)
