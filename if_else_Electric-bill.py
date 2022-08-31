if __name__=="__main__":

    unit=int(input("Input Total Unit: "))

    amt1 = (unit * 0.50);
    amt2 = (amt1 + (unit-50) * 0.75);
    amt3 = (amt2 + (unit-100) * 1.20);
    amt4 = (amt3 + (unit-250) * 1.50);

    if (unit <= 50):

        
        sur_char = (amt1 * 0.20);
        net_amt = (amt1 + sur_char);

        print("Total Bill: ", float(net_amt))

    elif (unit <= 150):

        
        sur_char = (amt2 * 0.20);
        net_amt = (amt2 + sur_char);

        print("Total Bill: ", float(net_amt))

    elif (unit <= 250):
        sur_char = (amt3 * 0.20);
        net_amt = (amt3 + sur_char);

        print("Total Bill: ", float(net_amt))

    elif (unit > 250):
        sur_char = (amt4 * 0.20);
        net_amt = (amt4 + sur_char);

        print("Total Bill: ", float(net_amt))

    else:
        print("Null")


        

        
