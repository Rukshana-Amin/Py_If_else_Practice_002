if __name__=="__main__":

    a=int(input("Input a: "))
    b=int(input("Input b: "))
    c=int(input("Input c: "))

    import math
    
    Discriminant=(b*b)-(4*a*c);

    if (Discriminant > 0):

        root1 = (-b + (math.sqrt(Discriminant)) / (2*a));
        root2 = (-b - (math.sqrt(Discriminant)) / (2*a));

        print("Root1 = ",int(root1))
        print("Root2 = ",int(root2))

    elif (Discriminant == 0):

        root1=root2= (-b / (2*a));
        print("root1= ", int (root1))

    elif (Discriminant < 0):

        root1 = (-b / (2*a));
        root2 = (-b / (2*a));

        print("Root1 = ",int(root1))
        print("Root1 = ",int(root1))

    else:

        print(Null)
        

        

    

    
