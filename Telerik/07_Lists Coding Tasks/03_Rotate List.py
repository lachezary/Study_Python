# Write a program that rotates a list several times 
# (the first element becomes last).

# list = 1,2,3,4,5 and N = 2 -> result = 3,4,5,1,2
# Note that N could be larger than the length of the list.

# list = 1,2,3,4,5 and N = 6 -> result = 2,3,4,5,1

rotate_list = input().split(",")

rotations = int(input())
char_rotation = ""

for i in range(rotations):
    char_rotation = rotate_list[0]
    rotate_list.append(char_rotation)
    rotate_list.pop(0)
    
my_string = ','.join(rotate_list)
print(my_string)