import random
a = int(input("enter the face of cion (0 head and 1 tail ) :"))
b = random.randint(0,1)
if(a == 1) :
    if(a == b) :
        print("this is correct,the Answer is tail ")
    else :
         print("this is wrong bro hhh")
elif(a == 0) :
        if(a == b) :
            print("this is correct, the Answer is head")
        else :
         print("this is wrong bro hhh")