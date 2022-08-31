if __name__=="__main__":

    ch= str(input("Enter value:"))

    if(ch >= 'A' and ch <= 'Z'):
        print(str(ch),"is uppercase alphabet")

    elif(ch >= 'a' and ch <= 'z'):
        print(str(ch),"is lowercase alphabet")

    else:
        print("Character is not alphabet")
        
