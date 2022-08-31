if __name__=="__main__":

    a=int(input("Input first side: "))
    b=int(input("Input second side: "))
    c=int(input("Input third side: "))

    if ((a+b>c) and (a+c>b) and (b+c>a)):
        print("Triangle is valid")

    else:
        print("Triangle is not valid")
        
    
