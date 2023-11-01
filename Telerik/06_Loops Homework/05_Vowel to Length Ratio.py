# The vowels are 'aouei'

# If two foods share the same ratio, choose the one with more vowels. 
# If they have the same ratio and same number of vowels, choose the one with more letters.

# Input
# The input consists of several lines
# On the first line - integer N - the number of lines to follow
# On the next N lines - each food
# Output
# Output the best food and its ratio in format `food vowels/letters'

foods_num = int(input())

vowel_a = 0
vowel_o = 0
vowel_u = 0
vowel_e = 0
vowel_i = 0
all_vowels = 0
ratio = 0
length = 0

new_food = input()
vowel_a = new_food.count("a")
vowel_o = new_food.count("o")
vowel_u = new_food.count("u")
vowel_e = new_food.count("e")
vowel_i = new_food.count("i")
all_vowels = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u
length = len(new_food)
ratio = all_vowels / length

old_all_vowels = all_vowels
old_ratio = ratio
old_length = length
old_food = new_food

for i in range (foods_num-1):
    new_food = input()
    vowel_a = new_food.count("a")
    vowel_o = new_food.count("o")
    vowel_u = new_food.count("u")
    vowel_e = new_food.count("e")
    vowel_i = new_food.count("i")
    all_vowels = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u
    length = len(new_food)
    ratio = all_vowels / length
    if ratio < old_ratio and all_vowels != 0:
        old_all_vowels = all_vowels
        old_ratio = ratio
        old_length = length
        old_food = new_food
    elif ratio == old_ratio and all_vowels > old_all_vowels:
        old_all_vowels = all_vowels
        old_ratio = ratio
        old_length = length
        old_food = new_food
    elif all_vowels == old_all_vowels and length > old_length:
        old_all_vowels = all_vowels
        old_ratio = ratio
        old_length = length
        old_food = new_food

print(f"{old_food} {old_all_vowels}/{old_length}")
            
    
