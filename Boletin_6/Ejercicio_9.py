'''
numero=6

for i in range (1, numero):
    
    if numero%i==0:
        i+=i       
        if numero==i:
            print("es un numero perfecto")
'''

numero=int(input("Ingrese un numero mayor que 0:"))
while numero<1:
    numero=int(input("Numero inavalido, ingrese un numero mayor que 0:"))
    
total=0
for i in range (1, (numero//2)+1):

    if numero%i==0:
        total+=i
        
if total==numero:
    print(f"{numero} es un numero perfecto")
else:
    print(f"{numero} no es un numero perfecto")