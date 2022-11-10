

cantidad=int(input("Cuantos numero desea introducir?:"))

while cantidad<=0:
    cantidad=int(input("Cuantos numero desea introducir?:"))

total=0
for i in range(cantidad):
    numero=int(input("introduce un numero mayor que 0:"))
    while numero<=0:
        numero=int(input("numero no valido,introduce un numero mayor que 0:"))
    total+=numero
    
print(f"La media es{total/cantidad}")
'''
cantidad=int(input("Cuantos numero desea introducir?:"))

while cantidad<=0:
    cantidad=int(input("Cuantos numero desea introducir?:"))

total, contador =0, 0
while cantidad>contador:
    numero=int(input("introduce un numero mayor que 0:"))
    while numero<=0:
        numero=int(input("numero no valido,introduce un numero mayor que 0:"))
    contador+=1
    total+=numero
 '''   
    
print(f"La media es{total/cantidad}")










