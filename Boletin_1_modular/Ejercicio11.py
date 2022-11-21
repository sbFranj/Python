'''
Escribe una función intersect que reciba dos listas y devuelva otra lista con los
elementos que son comunes a ambas, sin repetir ninguno.
'''
lista_1=[1,2,3,4,5,6]
lista_2=[1,7,3,9,5,6]

def obtenerComunes(lista1, lista2):
    comunes=[]
    if len(lista1)>len(lista2):
        for i in range(len(lista1)):
            if lista1[i]==lista2[i]:
                comunes.append(lista1[i])
    else:
        for i in range(len(lista2)):
            if lista1[i]==lista2[i]:
                comunes.append(lista2[i])
    
    return comunes

print(obtenerComunes(lista_1, lista_2))