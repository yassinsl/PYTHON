input_str = input("Please enter numbers with space: ")
my_list_str = input_str.split(" ")
my_list = [int(x) for x in my_list_str]

max_num = my_list[0]  

for num in my_list:
    if num > max_num:
        max_num = num

print(f"The maximum number in the list is: {max_num}")
