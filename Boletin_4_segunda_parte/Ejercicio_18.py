linferior=int(input("Introduce limite inferior:"))
lsuperior=int(input("Introduce limite superior:"))

while linferior>=lsuperior:
    print("El limite inferior no puede ser mas grande que el limite superior!!!")
    linferior=int(input("Introduce limite inferior:"))
    lsuperior=int(input("Introduce limite superior:"))
    
num=int(input("Introduce numero:"))
suma=0
fuera=0
igual=0
while num!=0:
    
    if linferior<num<lsuperior:
        suma+=num
    elif num<linferior or num>lsuperior:
        fuera+=1   
    else:
        igual+=1
    
    num=int(input("Introduce numero:"))
    
print(f"La suma de los numeros dentro del intervalo es {suma}.", f"{fuera} numeros estan fuera del intervalo.", f"{igual} numeros han sido iguales.")
    