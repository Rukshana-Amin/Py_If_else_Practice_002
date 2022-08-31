if __name__=="__main__":

    a=int(input("Input first side: "))
    b=int(input("Input second side: "))
    c=int(input("Input third side: "))

    if (a == b and b == c):
        print("Triangle is equilateral triangle")

    elif ((a == b) or (a == c) or (b == c)):
        print("Triangle is Isosceles triangle")

    else:
        print("Triangle is Scalene triangle")
        
