"""
Author: YASSINE LAHSSINI
Date: 23/01/2024
Time: 10:46
"""
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
section_bar = "__ hello and welcome to the International auction __".upper()
print(" " * 15 + section_bar)

def print_price(name, price_bid):
    bid = {}
    bid[name] = price_bid
    return bid
#  I TOOK THIS FUNCTION FROM CHATGPT 
def max_price(bid_list):
    if not bid_list:
        print("No bids available.")
        return

    max_bid_dict = max(bid_list, key=lambda x: list(x.values())[0])
    max_bid = list(max_bid_dict.values())[0]
    max_bidder_name = list(max_bid_dict.keys())[0]

    print(f"The highest bid is from {max_bidder_name} with a price of {max_bid}")

bid_1 = []

while True:
    name = input("PLEASE ENTER YOUR NAME AND LAST NAME: ")
    price_bid = int(input("PLEASE ENTER THE PRICE YOU WANT TO BID AT: "))
    
    bid_1.append(print_price(name, price_bid))
    
    repeat = int(input("If you want to stop, print 0. Otherwise, print 1: "))
    if repeat == 1:
        clear_screen()
    elif repeat == 0:
        break
clear_screen()
max_price(bid_1)
