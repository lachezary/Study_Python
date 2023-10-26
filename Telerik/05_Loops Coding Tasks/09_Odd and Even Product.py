lines_input = int(input())

odd_lines = 1
even_lines = 1

for i in range(lines_input):
    num = int(input())
    if i % 2 != 0:
        odd_lines *= num
    else:
        even_lines *= num

if odd_lines == even_lines:
    print(f"yes {odd_lines}")
else:
    print(f"no {even_lines} {odd_lines}")
