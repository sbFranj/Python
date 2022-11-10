'''
Crea un programa que tras preguntar por dos números realice la división del mayor
de ellos por el menor y muestre el resultado de la división, es decir, el cociente y el
resto. Solo puedes utilizar la suma o la resta, pero no otras operaciones.
'''

num=int(input("Introduce numero: "))
num2=int(input("Introduce segundo numero: "))

resto=num
cociente=0

if num>num2:
    while resto>=0:
        resto-=num2
        cociente+=1
    
    print(f"{num}/{num2} es igual a {cociente-1}, con resto {resto+num2}")
  
resto=num2
cociente=0
    
if num2>num:
    while resto>=0:
        resto-=num
        cociente+=1
    
    print(f"{num2}/{num} es igual a {cociente-1}, con resto {resto+num}")

    