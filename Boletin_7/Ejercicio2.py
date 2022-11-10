'''
Diseñar un programa que pida dos números enteros y nos muestre los siguientes
números que son múltiplos del segundo introducido a partir del primero. Por ejemplo,
si introducimos:
                13 y 7 ⇒ 14, 21, 28, 35, 42, 49, 56, 63, 70, 77
                (a partir de 13 los siguientes 10 múltiplos de 7)
'''

num=int(input("Introduce numero: "))
num2=int(input("Introduce segundo numero: "))


contador=0
inicio=num
total=""
while contador<10:
    inicio+=1
    if inicio%num2==0:
        
         
        contador+=1
        if contador==10:
            total+=str(inicio)
        else:
            total+=str(inicio)+", "
            
print(f"{num} y {num2} => " + total)
    

    
