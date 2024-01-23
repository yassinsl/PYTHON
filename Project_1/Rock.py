import random
num =int(input("please enter a number (0 rock or 1 paper and 2 scissor) :  ")) 
list = ["rock", "paper", "scissor"]
index = len(list) - 1
rm = random.randint(0,index)
if(num < 0 and num > 2):
    print("you lose bro ??")
elif(num == 0):
    if(num == rm):
        print("same choose")
    elif(rm == 1):
        print(f"you win,the {list[1]} wins against {list[0]}")
    elif(rm == 2):
        print(f"you lose,the {list[0]} wins against {list[2]}")
elif(num == 1):
    if(num == rm):
        print("same choose")
    elif(rm == 0):
        print(f"you win,the {list[1]} wins against {list[0]}")
    elif(rm == 2):
        print(f"you lose,the {list[2]} wins against {list[1]}")
elif(num == 2):
    if(num == rm):
        print("same choose")
    elif(rm == 0):
        print(f"you lose,the {list[0]} wins against {list[2]}")
    elif(rm == 1):
        print(f"you win,the {list[2]} wins against {list[1]}")