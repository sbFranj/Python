'''
La secuencia siguiente está definida para el conjunto de los números enteros:

            n → n/2 (n es par)
            n → 3n + 1 (n es impar)
            
Utilizando la función anterior y empezando en 13 se genera la siguiente secuencia
de números:

        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Esta secuencia tiene 10 términos y se cree que cualquier secuencia termina en 1.
Elabora un programa que pida un número N e imprima una cadena con la secuencia
de números hasta llegar a 1.
'''
num=int(input("Introduce numero: "))
total=0
secuencia=""
recuerdo=num
lista=[]
while not(total==1):
    if num%2==0:
        total=num//2
        num=total
        secuencia +=" → "+ str(total)
        lista.append(total)
    else:
        total=num*3+1
        num=total
        secuencia +=" → "+ str(total) 
        lista.append(total)
print(" ")
print(f"Con lista: {recuerdo}->{lista}") 
       
print(f"Sin lista: {recuerdo}"+secuencia)
    