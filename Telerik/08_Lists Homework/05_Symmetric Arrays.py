# A symmetric array is one, where the element at 
# index x 
# is equal to the element at 
# index array.length - 1 - x.

# Input
# Read from the standard input.

# On the first line, read the number 
# N - the number of arrays to follow.
# On the N lines, read the elements of 
# each array, separated by white space.
# Output
# Print to the standard output.

# For each of the arrays, print Yes of the array 
# is symmetric, or No if it's not.

input_lines = int(input())

for _ in range (input_lines):
    array_test = input().split(" ")
    is_symmetric = True
    
    for i in range(len(array_test)//2):
        if array_test[i] != array_test[-1 -i]:
            is_symmetric = False
            break
        
        
    print("Yes" if is_symmetric else "No")