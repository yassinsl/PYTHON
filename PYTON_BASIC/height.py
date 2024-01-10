inp_user = input('Please enter the numbers of list with space :')
my_list_str = inp_user.split(' ')
my_list = [int(x) for x in my_list_str]
sum_list = 0
length_list = 0
for i in my_list :
    sum_list += i
    length_list += 1
else :
    avre_list = sum_list // length_list
    print(f"avrege the list is :{avre_list}")