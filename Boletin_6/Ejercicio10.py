
numero=int(input("introduce un numero entero positivo:"))

if numero==0 and numero==1:
    print("el factorial es 1")
while numero<0:
    numero=int(input("numero no valido introduzca un numero entero positivo:"))
    
total=1  
for i in range(numero):
    
    total*=i+1
    
print(f"factorial es {total}")