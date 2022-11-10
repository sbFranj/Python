'''
Escribir una función denominada encajan que indique si dos fichas de dominó
encajan o no. Las fichas son recibidas en dos cadenas de texto con el siguiente
formato

            [3,4] [2,5]
'''

ficha1=[1,4]
ficha2=[2,6]

def fichasEncajan(lista1, lista2):
    encajan=False
    if lista1[0]==lista2[0] or lista1[1]==lista2[1] or lista1[1]==lista2[0] or lista1[0]==lista2[1]:
        encajan=True
    
    return encajan

print (f"la ficha {ficha1} y la ficha {ficha2} encajan?", fichasEncajan(ficha1, ficha2))