import random

array = input("please enter names with point ex(yassin.achraf.ex) :") 
list = array.split(".")
index = len(list) - 1
i = 0
choose =random.randint(0,index)
while(i <= index):
    if(i == choose):
        print(f"sorry {list[i]}, this is a game. please Pay.")
    i+= 1