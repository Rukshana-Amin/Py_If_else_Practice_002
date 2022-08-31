if __name__=="__main__":

    year=int (input("Input Year: "))

    if (year % 400 == 0):
        print(int(year),"This is a leap year")

    elif ((year % 4 ==0) and (year % 100 !=0)):
        print (int(year), "This is a leap year")

    else:
        print(int(year), "This is not a leap year")
