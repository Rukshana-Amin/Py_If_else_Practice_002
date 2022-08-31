if __name__=="__main__":

    month=int(input("Input Month Number: "))

    '''January=1;
    February=2;
    March=3;
    April=4;
    May=5;
    June=6;
    July=7;
    August=8;
    September=9;
    October=10;
    November=11;
    December=12;'''

    if (month==1 or month==3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        print("It contains 31 days")

    elif (month == 2):
        print ("It contains 28/29 days")

    elif (month == 4 or month == 6 or month == 9 or month == 11):
        print("It contains 30days")

    else:
        print("Null")
        
    
