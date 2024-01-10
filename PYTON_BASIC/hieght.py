inp_user = input('Please enter the numbers of list with space: ')
my_list_str = inp_user.split(' ')
total_sum = 0
length = 0

for num_str in my_list_str:
    num = int(num_str)
    total_sum += num
    length += 1

average = total_sum / length
print(f"average is {average}")
