if __name__=="__main__":

    basic=float(input("Input Basic Salary: "))
    

    if (basic <= 10000):

        HRA = basic * 0.2;
        DA = basic * 0.8;

        gross=(basic + DA + HRA);

        print("Gross Salary is : ", float(gross))

    elif  ((basic >= 10001) and (basic <= 20000)):

        HRA = basic * 0.25;
        DA = basic * 0.9;

        gross=(basic + DA + HRA);

        print("Gross Salary is : ", float(gross))

    elif (basic >= 20001):

        HRA = basic * 0.3;
        DA = basic * 0.95;

        gross=(basic + DA + HRA);

        print("Gross Salary is : ", float(gross))

    else:
        print("Null")
        

    

        
