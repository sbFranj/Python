'''
Desarrolla un programa que a partir de una lista de números y un entero k, realice la
llamada a tres funciones: 
    a) para devolver una lista de números con los menores de k, 
    b) otra con los mayores 
    c) otra con aquellos que son múltiplos de k.
'''

listanumeros=[1,2,3,4,5,6,7,8,9,10]

k=5

def obtenerMenores(lista, numero):
    menores=[]
    for i in range(len(lista)):
        if lista[i]<numero:
            menores.append(lista[i])
    return menores
def obtenerMayores(lista, numero):
    mayores=[]
    for i in range(len(lista)):
        if lista[i]>numero:
            mayores.append(lista[i])
    return mayores
def obtenerMultiplos(lista, numero):
    multiplos=[]
    for i in range(len(lista)):
        if lista[i]%numero==0:
            multiplos.append(lista[i])
    return multiplos

print("a)", obtenerMenores(listanumeros, k)) 
print("b)", obtenerMayores(listanumeros, k))
print("c)", obtenerMultiplos(listanumeros, k))




       