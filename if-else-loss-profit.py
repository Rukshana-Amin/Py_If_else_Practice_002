if __name__=="__main__":

    CP=int (input("Input Cost Price: "))
    SP=int (input("Input Selling Price: "))

    P=(SP-CP);
    L=(CP-SP);

    if (SP > CP):

        print("Profit: ", int (P))

    elif (CP > SP):

        print("Loss: ", int(L))

    else:
        print("Null")



        
