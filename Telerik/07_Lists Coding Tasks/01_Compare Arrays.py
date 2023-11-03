
# input_lines = int(input())
# array_a = ""
# array_b = ""


# for i in range (input_lines):
#     element_input = input()
#     array_a = array_a + element_input
    
# for i in range (input_lines):
#     element_input = input()
#     array_b = array_b + element_input    
    
# array_a = int(array_a)
# array_b = int(array_b)

# if array_a == array_b:
#     print("equal")
# else:
#     print("not equal")  


input_lines = int(input())
array_a = []
array_b = []

for i in range(input_lines):
    new_value = input()
    array_a.append(new_value)

for i in range(input_lines):
    new_value = input()
    array_b.append(new_value)

if array_a == array_b:
    print("equal")
else:
    print("not equal")  