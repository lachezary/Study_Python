# Input
# On the only line you will receive all the numbers to be sorted.
# Output
# On the only line of output, print all the numbers sorted in format n1, n2, n3, .. n

num_list = input().split(", ")
num_list = list(map(int, num_list))

sorted_list = num_list.copy()
sorted_list.sort(reverse=True)

print(", ".join(map(str, sorted_list)))