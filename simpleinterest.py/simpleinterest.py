def simpInt(Principal, Rate, Time):
    return(Principal * Rate * Time) / 100
    
if __name__ == "__main__":
    P = int(input("Enter the Principal amount: "))
    i = int(input("Enter the Rate of interest: "))
    t= int(input("Enter the Time in years: "))
    
    print(" Simple Interest : ", simpInt(P, i, t))