grupo=input("Inotroduce grupo sanguineo(A, B, AB, 0):")
while grupo!="A" and grupo!="B" and grupo!="AB" and grupo!="0":
    print("Introduzca un grupo sanguineo valido!")
    grupo=input("Inotroduce grupo sanguineo(A, B, AB, 0):")
    
rh=input("Introduce Rh(+, -):")
while rh!="+" and rh!="-":
    print("Introduzca un rh valido!")
    rh=input("Introduce Rh(+, -):")
    
grupo2=input("Inotroduce grupo sanguineo(A, B, AB, 0):")
while grupo2!="A" and grupo2!="B" and grupo2!="AB" and grupo2!="0":
    print("Introduzca un grupo sanguineo valido!")
    grupo=input("Inotroduce grupo sanguineo(A, B, AB, 0):")
    
rh2=input("Introduce Rh(+, -):")
while rh2!="+" and rh2!="-":
    print("Introduzca un rh valido!")
    rh2=input("Introduce Rh(+, -):")

if rh=="+" and rh2=="+":
    if grupo=="A" and grupo2=="A":
        print("Son compatibles, A+ es receptor/donador de A+")
    elif grupo=="A" and grupo2=="AB":
        print("Son compatibles, A+ es donador de AB+")
    elif grupo=="A" and grupo2=="0":
        print("Son compatibles, A+ es receptor de 0+")
    
    if grupo=="B" and grupo2=="B":
        print("Son compatibles, B+ es receptor/donador de B+")
    elif grupo=="B" and grupo2=="AB":
        print("Son compatibles, B+ es donador de AB+")
    elif grupo=="B" and grupo2=="0":
        print("Son compatibles, B+ es receptor de 0+")
        
    if grupo=="AB" and grupo2=="AB":
        print("Son compatibles, AB+ es receptor/donador de AB+")
    elif grupo=="AB" and grupo2=="A":
        print("Son compatibles, AB+ es receptor de A+")
    elif grupo=="AB" and grupo2=="B":
        print("Son compatibles, AB+ es receptor de B+")
    elif grupo=="AB" and grupo2=="0":
        print("Son compatibles, AB+ es receptor de 0+")
    
    if grupo=="0" and grupo2=="0":
        print("Son compatibles, 0+ es receptor/donador de 0+")
    elif grupo=="0" and grupo2=="A":
        print("Son compatibles, 0+ es donador de A+")
    elif grupo=="AB" and grupo2=="B":
        print("Son compatibles, 0+ es donador de B+")
    elif grupo=="0" and grupo2=="AB":
        print("Son compatibles, 0+ es donador de AB+")
elif rh=="-" and rh2=="-":
    if grupo=="A" and grupo2=="A":
        print("Son compatibles, A- es receptor/donador de A-")
    elif grupo=="A" and grupo2=="AB":
        print("Son compatibles, A- es donador de AB-")
    elif grupo=="A" and grupo2=="0":
        print("Son compatibles, A- es receptor de 0-")
    
    if grupo=="B" and grupo2=="B":
        print("Son compatibles, B- es receptor/donador de B-")
    elif grupo=="B" and grupo2=="AB":
        print("Son compatibles, B- es donador de AB-")
    elif grupo=="B" and grupo2=="0":
        print("Son compatibles, B- es receptor de 0-")
        
    if grupo=="AB" and grupo2=="AB":
        print("Son compatibles, AB- es receptor/donador de AB-")
    elif grupo=="AB" and grupo2=="A":
        print("Son compatibles, AB- es receptor de A-")
    elif grupo=="AB" and grupo2=="B":
        print("Son compatibles, AB- es receptor de B-")
    elif grupo=="AB" and grupo2=="0":
        print("Son compatibles, AB- es receptor de 0-")
    
    if grupo=="0" and grupo2=="0":
        print("Son compatibles, 0- es receptor/donador de 0-")
    elif grupo=="0" and grupo2=="A":
        print("Son compatibles, 0- es donador de A-")
    elif grupo=="AB" and grupo2=="B":
        print("Son compatibles, 0- es donador de B-")
    elif grupo=="0" and grupo2=="AB":
        print("Son compatibles, 0- es donador de AB-")
    
elif rh=="+" and rh2=="-":
    if grupo=="A" and grupo2=="A":
        print("Son compatibles, A+ es receptor de A-")
    elif grupo=="A" and grupo2=="0":
        print("Son compatibles, A+ es receptor de 0-")
    
    if grupo=="B" and grupo2=="B":
        print("Son compatibles, B+ es receptor de B-")
    elif grupo=="B" and grupo2=="0":
        print("Son compatibles, B+ es receptor de 0-")
        
    if grupo=="AB" and grupo2=="AB":
        print("Son compatibles, AB+ es receptor de AB-")
    elif grupo=="AB" and grupo2=="A":
        print("Son compatibles, AB+ es receptor de A-")
    elif grupo=="AB" and grupo2=="B":
        print("Son compatibles, AB+ es receptor de B-")
    elif grupo=="AB" and grupo2=="0":
        print("Son compatibles, AB+ es receptor de 0-")
    
    if grupo=="0" and grupo2=="0":
        print("Son compatibles, 0+ es receptor de 0-")
elif rh=="-" and rh2=="+":
    if grupo=="A" and grupo2=="A":
        print("Son compatibles, A- es donador de A+")
    elif grupo=="A" and grupo2=="AB":
        print("Son compatibles, A- es donador de AB+")
    
    if grupo=="B" and grupo2=="B":
        print("Son compatibles, B- es donador de B+")
    elif grupo=="B" and grupo2=="AB":
        print("Son compatibles, B- es donador de AB+")
      
    if grupo=="AB" and grupo2=="AB":
        print("Son compatibles, AB- es donador de AB+")
    
    if grupo=="0" and grupo2=="0":
        print("Son compatibles, 0- es donador de 0+")
    elif grupo=="0" and grupo2=="A":
        print("Son compatibles, 0- es donador de A+")
    elif grupo=="AB" and grupo2=="B":
        print("Son compatibles, 0* es donador de B+")
    elif grupo=="0" and grupo2=="AB":
        print("Son compatibles, 0- es donador de AB+")
else:
    print("No son compatibles")