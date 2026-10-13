def simpInt(Principal, Rate, Time):
    return(Principal * Rate * Time) / 100
    
if __name__ == "__main__":
    P = int(sys.argv[1])
    i = int(sys.argv[2])
    t = int(sys.argv[3])

    print(" Simple Interest : ", simpInt(P, i, t))