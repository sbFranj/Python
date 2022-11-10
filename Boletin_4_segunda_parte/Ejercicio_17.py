num=int(input("inserte primer numero:"))
num2=int(input("inserte segundo numero:"))

while num>num2:
    print("inserte un rango de numeros de menor a mayor")
    num=int(input("inserte primer numero:"))
    num2=int(input("inserte segundo numero:"))
for a in range(num, num2+1):   
    if a%2==0:
        print(a)