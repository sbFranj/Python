'''
Diseñar un programa que muestre, para cada número introducido por teclado, si es
par, si es positivo y su cuadrado. El proceso se repetirá hasta que el número
introducido por teclado sea 0. Por ejemplo:

    4 ⇒ es par, positivo y su cuadrado es 16
    -7 ⇒ es impar, negativo y su cuadrado es 49
'''
num=int(input("Introduce num: "))

while num!=0:
    if num%2==0 and num>0:
        print(f"El numero {num} es par, positivo y su cuadrado es {num*num}")
        
    elif num%2==0 and num<0:
        print(f"El numero {num} es par, negativo y su cuadrado es {num*num}")
        
    elif num%2==1 and num<0:
        print(f"El numero {num} es impar, positivo y su cuadrado es {num*num}")
        
    else:
        print(f"El numero {num} es impar, negativo y su cuadrado es {num*num}")
    num=int(input("Introduce num: ")) 
    