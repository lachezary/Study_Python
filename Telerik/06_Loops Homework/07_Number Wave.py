# On the first line, you will receive the number N.
# Output
# Print a "wave" i.e. the numbers from 1 to N and then the numbers 
# from N - 1 to 1 on a single line separated by space.
# Constraints
# 1 <= N <= 1000

wave_num = int(input())

for i in range (wave_num):
    print(f"{i+1}", end=' ')
    
for i in range (wave_num-1, 0, -1):
    print(f"{i}", end=' ')
    