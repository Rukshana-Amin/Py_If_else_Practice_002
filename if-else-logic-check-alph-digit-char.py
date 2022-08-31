if __name__=="__main__":

    ch=input("Enter value: ")

    if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
        print("This is an alphabet")

    elif (ch>= '0' and ch <='9'):
        print("This is a digit")

    else:
        print ("This is a special character")
        

    
