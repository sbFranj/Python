'''
dia=dia=int(input("Introduce dia:"))
while dia<0 and dia>31:
    print("Rango de dias incorrecto")
    dia=int(input("Introduce dia:"))
    
mes=int(input("Introduce mes:"))
while mes<0 and mes>12:
    print("Rango de mes incorrecto")
    mes=int(input("Introduce mes:"))


total=(mes*30)-(30-dia)

print(total)
'''    
dia=dia=int(input("Introduce dia:"))
while dia<0 and dia>31:
    print("Rango de dias incorrecto")
    dia=int(input("Introduce dia:"))
    
mes=int(input("Introduce mes:"))
while mes<0 and mes>12:
    print("Rango de mes incorrecto")
    mes=int(input("Introduce mes:"))

anio=int(input("Introduce año:"))
while anio<0:
    print("Rango de año incorrecto")
    anio=int(input("Introduce año"))
    
    
if (anio%4==0) or ((not(anio%100==0)) and (anio%600==0)):    
    if mes==1:
        print(31-(31-dia))   
        
    elif mes==2:
        
        if dia==30:
            print(31+29-(27-dia))
        elif dia==31:
            print(31+29-(26-dia))
        print(31+28-(29-dia))
    
    elif mes==3:
        print(59+31-(31-dia))
    
    elif mes==4:
        print(90+30-(30-dia))
    
    elif mes==5:
        print(120+31-(31-dia))    
    
    elif mes==6:
        print(151+30-(30-dia))
        
    elif mes==7:
        print(181+31-(31-dia))
        
    elif mes==8:
        print(212+31-(31-dia))
    
    elif mes==9:
        print(243+30-(30-dia))
    
    elif mes==10:
        print(273+31-(31-dia))
    
    elif mes==11:
        print(304+30-(30-dia))
    
    elif mes==12:
        print(334+31-(31-dia))

else:
    if mes==1:
        print(31-(31-dia))   
    
    elif mes==2:
        if dia==29:
            print(31+28-(27-dia))
        elif dia==30:
            print(31+28-(26-dia))
        elif dia==31:
            print(31+28-(25-dia))
        print(31+28-(28-dia))
    
    elif mes==3:
        print(59+31-(31-dia))
    
    elif mes==4:
        print(90+30-(30-dia))
    
    elif mes==5:
        print(120+31-(31-dia))    
    
    elif mes==6:
        print(151+30-(30-dia))
        
    elif mes==7:
        print(181+31-(31-dia))
        
    elif mes==8:
        print(212+31-(31-dia))
    
    elif mes==9:
        print(243+30-(30-dia))
    
    elif mes==10:
        print(273+31-(31-dia))
    
    elif mes==11:
        print(304+30-(30-dia))
    
    elif mes==12:
        print(334+31-(31-dia))
        
    
    
    
    
    
    
    
    
    
    
    