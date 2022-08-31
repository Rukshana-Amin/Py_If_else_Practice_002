if __name__=="__main__":

    num=int (input ("Input number: "))


    if ((num % 5 ==0) and (num % 11 ==0)):
        print("The number is divisible by both 5 & 11")

    elif (num % 5 == 0):
        print("The number is divisible by 5")

    elif (num % 11 ==0):
        print("The number is divisible by 11")

    else:
        print(" The number is not divisible by 5 & 11")
        
