dia=int(input("Introduce dia:"))

while dia<0 or dia>31:
    print("numero de dia no valido")
    dia=int(input("Introduce dia:"))
    
    
mes=int(input("Introduce mes:"))

while mes<0 or mes>12:
    print("numero de mes no valido")
    mes=int(input("Introduce mes:"))
    
    
hemisferio=input("Introduce hemisferio(N/S):")

while not(hemisferio!="s" or hemisferio!="S" or hemisferio!="n" or hemisferio!="N"):
    print("Hemisferio no valido:")
    hemisferio=input("Introduce hemisferio(N/S):")

if hemisferio=="N" or hemisferio=="n":

    if mes==9 and dia>22:#Otoño
        print("Hemisferio norte, Otoño")
    elif mes==10 or mes==11:
        print("Hemisferio norte, Otoño")
    elif mes==12 and dia<21:
        print("Hemisferio norte, Otoño")
    
    if mes==12 and dia>20:#Invierno
        print("Hemisferio norte, Invierno")
    elif mes==1 or mes==2:
        print("Hemisferio norte, Invierno")
    elif mes==3 and dia<21:
        print("Hemisferio norte, Invierno")
        
    if mes==3 and dia>20:#Primavera
        print("Hemisferio norte, Primavera")
    elif mes==4 or mes==5:
        print("Hemisferio norte, Primavera")
    elif mes==6 and dia<21:
        print("Hemisferio norte, Primavera")
    
    if mes==6 and dia>20:#Verano
        print("Hemisferio norte, Verano")
    elif mes==7 or mes==8:
        print("Hemisferio norte, Verano")
    elif mes==9 and dia<=22:
        print("Hemisferio norte, Verano")
        
elif hemisferio=="S" or hemisferio=="s":

    if mes==9 and dia>22:#Primavera
        print("Hemisferio norte, Primavera")
    elif mes==10 or mes==11:
        print("Hemisferio norte, Primavera")
    elif mes==12 and dia<21:
        print("Hemisferio norte, Primavera")
    
    if mes==12 and dia>20:#Verano
        print("Hemisferio norte, Verano")
    elif mes==1 or mes==2:
        print("Hemisferio norte, Verano")
    elif mes==3 and dia<21:
        print("Hemisferio norte, Verano")
        
    if mes==3 and dia>20:#Otoño
        print("Hemisferio norte, Otoño")
    elif mes==4 or mes==5:
        print("Hemisferio norte, Otoño")
    elif mes==6 and dia<21:
        print("Hemisferio norte, Otoño")
    
    if mes==6 and dia>20:#Invierno
        print("Hemisferio norte, Invierno")
    elif mes==7 or mes==8:
        print("Hemisferio norte, Invierno")
    elif mes==9 and dia<=22:
        print("Hemisferio norte, Invierno")
        