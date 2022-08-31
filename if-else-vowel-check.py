if __name__=="__main__":

    ch=str (input("Enter a value: "))

    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        print("This is a vowel")

    elif(ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        print("This is a vowel")

    elif ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
        print("This is a Consonant")

    else:
        print("This is not an alphabet")
        
