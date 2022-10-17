num=int(input("Introduzca numero:"))

while num<=0:
    print("El numero debe ser mayor que 0")
    num=int(input("Introduzca numero:"))
    
for i in range(1, num+1):
    if (i==2 or i%2!=0) and (i==3 or i%3!=0) and (i==5 or i%5!=0) and (i==7 or i%7!=0) and (i==11 or i%11!=0) and (i==13 or i%13!=0)and (i==17 or i%17!=0)and (i==19 or i%19!=0)and (i==23 or i%23!=0)and (i==29 or i%29!=0)and (i==31 or i%31!=0):
        print(i)