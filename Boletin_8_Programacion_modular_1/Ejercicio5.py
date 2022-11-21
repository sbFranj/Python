'''
Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’,
‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].
'''
print("a: Con la funcion externa 'reverse'")
lista=["Di","buen","dia", "a", "papa"]
lista.reverse()
print(lista)
print(" ")
print("b: Sin la funcion externa 'reverse'")

lista=["Di","buen","dia", "a", "papa"]

def riversada(lista):
    cadena=" "
    for i in range (len(lista)):
        cadena+=lista[(i+1)*-1]+" "
    return cadena
print(riversada(lista))

print(" ")
print("c: Con la funcion 'riversada'")

lista=["Di","buen","dia", "a", "papa"]

def riversada(lista):
    listainversa=[]
    for i in range (len(lista)):
        listainversa.append(lista[(i+1)*(-1)])
    return listainversa

print(riversada(lista))

