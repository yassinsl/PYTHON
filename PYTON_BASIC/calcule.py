num_1 = int(input("Please enter a number_1 : "))
num_2 = int(input("Please enter a number_2 : "))
cl = int(input("Please enter 1 to addetion or 2 to subtraction 3 to multiplecation or 4 to modelation or 5 to devision : "))
if(cl == 1):
    print(f"add is {num_1 + num_2}")
elif(cl == 2):
    print(f"sub is {num_1 - num_2}")
elif(cl == 3):
    print(f"mul is {num_1 * num_2}")
elif(cl == 4):
    print(f"mod is {num_1 % num_2}")
elif(cl == 5):
    print(f"mod is {num_1 // num_2}")