num = int(input("Please enter a number to play  FIZZ_BAZZ :"));
range = range(1 , num + 1);
for i in range:
    if(i % 3 == 0) :
        if(i % 3 == 0 and i % 5 == 0) :
            print("FIZZ_BAZZ")
        else :
            print("FIZZ")
    elif(i % 5 == 0) :
        print("BAZZ")
    else :
        print(i)
