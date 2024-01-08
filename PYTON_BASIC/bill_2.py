import random

array = input("please enter names with point ex(yassin.achraf.ex) :") 
list = array.split(".")
length = len(list)
choose =random.randint(1,length)
if choose == 1 :
    print(f"sorry {list[0]}, this is a game. please Pay.")
elif choose == 2 :
     print(f"sorry {list[1]}, this is a game. please Pay.")
elif choose == 3 :
     print(f"sorry {list[2]}, this is a game. please Pay.")
elif choose == 4 :
     print(f"sorry {list[3]}, this is a game. please Pay.")
elif choose == 5 :
     print(f"sorry {list[4]}, this is a game. please Pay.")