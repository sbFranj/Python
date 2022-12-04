'''
Diseñar una función que determine la cantidad de vocales diferentes, que tiene una palabra
o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2.
'''


def contar_vocales(palabra):
    recuento=""
    contador=0
    for i in range(len(palabra)):
        if ("a" in palabra) and ("a" not in recuento):
            contador+=1
            recuento+="a"
        elif ("e" in palabra) and ("e" not in recuento):
            contador+=1
            recuento+="e"
        elif ("i" in palabra) and ("i" not in recuento):
            contador+=1
            recuento+="i"
        elif ("o" in palabra) and ("o" not in recuento):
            contador+=1
            recuento+="o"
        elif ("u" in palabra) and ("u" not in recuento):
            contador+=1
            recuento+="u"
    
    return contador

palabras=input("introduce una palabra: ")
print (contar_vocales(palabras))

