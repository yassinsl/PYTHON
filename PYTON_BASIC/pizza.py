print("hello MS OR MST")
size_1 = input("how the size the pizza you want print first charcter (s/m/l) :")
total = 0;
if(size_1 == 's' or size_1 == 'S'):
    total = 25
    print(f"the price to small pizza is {total} DH")
elif(size_1 == 'm' or size_1 == 'M') :
    total = 55
    print(f"the price to meduim pizza is {total} DH")
elif(size_1 == 'l' or size_1 == 'L') :
    total = 90
    print(f"the price to large pizza is {total} DH")
    
APPEND = int(input("Want to add pepperoni enter(1 or 0) :"))
if(APPEND == 1) :
    if(total == 25 or total == 55) :
        total += 10
        print("price the pepperoni is 10 DH")
    elif(total ==90) :
        total += 20
        print("price the pepperoni is 20 DH")

cheese = int(input("Want to add cheese enter(1 or 0) :"))
if(cheese == 1) :
    total += 15
    print("price the chesse is 15 DH")
save = input("do you want to save this things print(yes) not print(no) : ")
if(save == 'yes') :
    print(f"price the total to buy is {total}")
else :
    print("I d'ont save this things")

print("thank you and welcome any time ")