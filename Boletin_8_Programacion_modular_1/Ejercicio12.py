'''
Escribe una función unionListas que reciba dos listas y devuelva los elementos que
pertenecen a una, o bien, a la otra, pero sin repetir ninguno (unión de conjuntos).

'''
lista_1=["a","b","c","d","e",6,"f"]
lista_2=[1,2,3,4,5,6,"f"]


def unionListas(lista1, lista2):
    union=[]
    for i in range(len(lista1)):
        if lista1[i]!=lista2[i]:
            union.append(lista1[i])
            union.append(lista2[i])
    
    return union

print(unionListas(lista_1, lista_2))