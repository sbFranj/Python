num=int(input("Introduce numero del 0 al 100:"))

while num<0 or num>100:
    print("Numero invalido")
    num=int(input("Introduce numero del 0 al 100:"))    

if 90<=num<=100:
    print("90-100, Sobresaliente.")
elif 70<=num<=89:
    print("70-89, Notable.")
elif 60<=num<=69:
    print("60-69, Bien.")
elif 50<=num<=59:
    print("50-59, Suficiente.")
else:
    print("0-49, Suspenso.")