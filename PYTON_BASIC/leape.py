years = int(input("please enter a years :"))

if(years % 4 == 0):
    if(years % 100 == 0):
        if(years % 400 == 0):
            print("this year is leap")
        else :print("this year is not leap")
    else :print("this year is not leap")
else :
    print(f"this year {years} not leap")