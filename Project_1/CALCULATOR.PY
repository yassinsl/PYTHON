"""
Author: YASSINE LAHSSINI
Date: 24/01/2024
Time: 02:18
"""
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator(num_1, num_2,operator):
    num_3 = 0
    match operator:
        case '+':
            num_3 = num_1 + num_2
        case '-':
            num_3 = num_1 - num_2
        case '/':
            num_3 = num_1 / num_2
        case '//':
            num_3 = num_1 // num_2
        case '*':
            num_3 = num_1 * num_2
        case '**':
            num_3 = num_1 ** num_2
        case '&':
            num_3 = num_1 & num_2
        case '^':
            num_3 = num_1 ^ num_2
        case '|':
            num_3 = num_1 | num_2
    return num_3;
print(" " * 25 + "__WELCOME TO MY CALCULATOR PROJECT__")
print()

num_1 = int(input("please enter a number 1 :"))
operator = input("please enter a operator like this(/,+,-,//,**,&,^,|) : ")
num_2 = int(input("please enter a number 2 :"))
num_3 = calculator(num_1,num_2,operator)
print("{} {} {} = {}".format(num_1,operator,num_2,num_3))
while True :
    num_5 = 0
    user_input = input("Do you want to continue? (yes/no): ")
    if(user_input == "yes"):
         num_4 = int(input("please enter a number if you want :"))
         operator = input("please enter operator if you want :")
         num_5 = calculator(num_3,num_4,operator)
         clear_screen()
         print("{} {} {} = {}".format(num_3,operator,num_4,num_5))
    else :
        break