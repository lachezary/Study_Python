# Write a method that reverses the digits of a 
# given decimal number.

# Input
# On the first line you will receive a number
# Output
# Print the given number with reversed digits

# normal_num = input()
# reversed_num = ""

# for char in normal_num:
#     reversed_num = str(char) + reversed_num
    
    
# print(reversed_num)
    


normal_num = input()
work_list = list(normal_num)
work_list.reverse()

reversed_num = "".join(work_list)

print(reversed_num)