# Input
# On a single line you will receive numbers 
# separated by space
# Output
# Print "yes" if the array is in Wave Form - 
# e.g. first > second < third > fourth < fifth >
# Print "no" if the array is not in Wave Form

wave_line = input().split(" ")

wave_line_int = list(map(int, wave_line))
is_wave = True

for i in range(0, len(wave_line_int), 2):
    if i + 1 < len(wave_line_int):
        odd_index_num = wave_line_int[i]
        even_index_num = wave_line_int[i+1]
        if odd_index_num > even_index_num:
            continue
        else:
            is_wave = False
            break

print("yes" if is_wave else "no")