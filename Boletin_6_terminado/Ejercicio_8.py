
num=int(input("insertar numero:"))
peque=num
while input("Quieres insertar mas numeros?(S/N):").upper()=="S":
    num=int(input("insertar numero:"))
    
    if num<peque: 
        peque=num
print(peque)