
cantidad=int (input("¿Cuantos numeros vas a introducir?"))

y=0

while y<cantidad:
    num=int(input("Introduce un numero mayor que 0:"))
    if num<=0:
        print("el numero no es valido, debe ser mayor que 0")
        num=int(input("Introduce un numero mayor que 0:"))
    if num%2==0:
        print(f"el {num} es par")
        y+=1
    else:
        print(f"el {num} es impar")
        y+=1
    
        
        