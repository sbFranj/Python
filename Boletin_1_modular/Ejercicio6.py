'''
Diseña una función llamada estaOrdenada que reciba una lista de elementos y
devuelva True si está ordenada o False en caso contrario
'''

lista1=[1, 10, 4, 16, 6, 7, 8, 9]
lista2=[1, 2, 3, 4, 5]

def listaOrdenada(lista):
    ordenada=False
    contador=0    
    for i in range(0, len(lista)):
        if lista[i]>lista[i-1]:
            contador+=1
    if contador==(len(lista)-1):
        ordenada=True           
    
    return ordenada

print("La lista 1 está ordenada?", listaOrdenada(lista1))
print("La lista 2 está ordenada?", listaOrdenada(lista2))


            


                