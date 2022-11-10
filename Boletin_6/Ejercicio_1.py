for a in range(0, 101):
    if (a%7==0) and (a%13==0):
        print(a, "es multiplo de 7 y de 13")
    
    elif (a%7==0):
        print(a, "es multiplo de 7")
    elif (a%13==0):
        print(a, "es multiplo de 13")