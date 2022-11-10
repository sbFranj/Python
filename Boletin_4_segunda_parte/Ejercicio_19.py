a=int(input("inserte primer numero:"))
b=int(input("inserte segundo numero:"))
f=1
acumulador=a

while f<b:
    f=f+1
    a=a*acumulador
    
    if f==b:
        print(f"La potencia es {a}")