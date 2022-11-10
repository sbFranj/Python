'''
a=int(input("inserte primer numero:"))
b=int(input("inserte segundo numero:"))
f=1
acumulador=a

while f<b:
    f=f+1
    a=a+acumulador
    
    if f==b:
        print(f"el producto es {a}")

'''
numA=int (input("Introduce numero:"))
numB=int (input("Introduce numero:"))

producto=0

if numA<0:    
    numA=-numA
    numB=-numB

for i in range(numA):    
    producto= producto + numB
print(f"El prodcturo es {producto}")
'''
elif numA<0:
    for i in range(numA*(-1)):    
        producto= producto + numB
    print(f"El prodcturo es {producto*-1}")
elif numB<0:
    for i in range(numA):    
        producto= producto + numB*(-1)
    print(f"El prodcturo es {producto*-1}")
elif numB<0 and numA<0:
    for i in range(numA*(-1)):    
        producto= producto + numB*(-1)
    print(f"El prodcturo es {producto*-1}")

'''



