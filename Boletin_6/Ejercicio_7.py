cantidad=int(input("cuantos numeros quieres introducir?:"))

while cantidad<=1:
    cantidad=int(input("Introduce mas de 1 numero,cuantos numeros quieres introducir?:"))

total=0
for i in range(cantidad):
    num=int(input("Introduce numero mayor que 0:"))
    while num<=0:
        num=int(input("numero no valido, introduce numero mayor que 0:"))
    
    total+=num

print(f"la media es {total/cantidad}")
        
