'''
Escribir una función que, devuelva el número de palabras que hay en una cadena que recibe
como parámetro. Ten en cuenta que entre dos palabras puede haber más de un blanco.
También al principio y al final de la frase puede haber blancos redundantes.
Por ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3
'''


def contar_palabras(frase):
    contador=0
    espaciodoble=0
    for i in range(len(frase)):
        if (" " in frase[i]):
            contador+=1
    for i in range(len(frase)-1):
        if (" " in frase[i]and " " in frase[i+1]):
           espaciodoble+=1  
    if (" " in frase[-1]):
        contador-=1
    if " " in frase[0]:
        contador-=1
    return contador+1-(espaciodoble)

print (contar_palabras("He estudiado mucho"))
print (contar_palabras("     He estudiado     mucho enserio    man    "))


