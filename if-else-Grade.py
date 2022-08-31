if __name__=="__main__":

    phy=float(input("Input marks of phy: "))
    chem=float(input("Input marks of chem: "))
    bio=float(input("Input marks of bio: "))
    math=float(input("Input marks of math: "))
    comp=float(input("Input marks of comp: "))

    per=((phy + chem + bio + math + comp) / 5.0);

    if (per >= 90):

        print("Grade A")

    elif (per >= 80):
        print("Grade B")

    elif (per >= 70):
        print("Grade C")

    elif (per >= 60):
        print("Grade D")

    elif (per >= 40):
        print("Grade E")

    elif (per < 40):
        print("Grade F")

    else:
        print("No Grade")
        

        
