from math import inf


num_list = input().split(" ")

big = 0
bigger = 0

for i in range (len(num_list)):
    if bigger == 0:
        bigger = int(num_list[i]) 
        big = bigger
    elif int(num_list[i]) > bigger:
        big = bigger
        bigger = int(num_list[i]) 
    elif int(num_list[i]) > big:
        big = int(num_list[i])
        
        
print(f"{bigger} {big}")
