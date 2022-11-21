
from random import randint

lista1=[]
rango=100
for i in range (rango):
    lista1.append(randint(0, 1000))

def obtenerElementoMayor(lista):
    mayor=lista[0]
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
        
    return mayor

def obtenerElementoMenor(lista):
    menor=lista[0]
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]
        
    return menor

def obtenerElementoSuma(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
        
    return suma

def obtenerElementoSustituto(lista, ls, vc):
    for i in range(len(lista)):
        if lista[i]==ls:
            lista[i]=vc           
        
    return lista

print("a. Mayor:", obtenerElementoMayor(lista1))
print("b. Menor:", obtenerElementoMenor(lista1))
print("c. Suma:", obtenerElementoSuma(lista1))
print("d. Media:", (obtenerElementoSuma(lista1)/rango))
print("f. Todos:    ", lista1)
print("e. Sustituir:", obtenerElementoSustituto(lista1, 69, 5))





