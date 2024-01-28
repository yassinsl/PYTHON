"""
Author: YASSINE LAHSSINI
Date: 25/01/2024
Time: 12 : 20
"""

from welcome import *

def coffe_puy(choose_user):
    total_coins = 0
    while True:
        coins_1 = int(input("How many 5 RS.coins :"))
        coins_2 = int(input("How many 10 RS.coins :"))
        coins_3 = int(input("How many 20 RS.coins :"))
        break;
    if choose_user == "latte": 
        total_coins = coins_1 + coins_2 + coins_3
    else:
        total_coins = coins_1 * 5 + coins_2 * 10 + coins_3 * 20
    print(f"Total coins is {total_coins}")
    print(f"here the {choose_user},Enjoy your coffee!")

print(welcome)
while True:
    choose_user = input("what would you like to have (latte/expresso/cappuccino): ")
    if choose_user == "off" :
        break;
    else :
        coffe_puy(choose_user)