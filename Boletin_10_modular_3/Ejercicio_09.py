'''
Crear una función que, tomando una cadena de texto como entrada, construya y devuelva
otra cadena formada de la siguiente manera: el método debe colocar todas las consonantes
al principio y todas las vocales al final de la misma, eliminando los blancos.
Por ejemplo, pasándole la cadena "curso de programacion", una posible solución sería
"crsdprgrmcnuoeoaaio
'''
def contar_vocales(palabra):
    salidav=""
    salidac=""
    for i in range(len(palabra)):
        if ("a" in palabra[i]) or ("e" in palabra[i])or ("i" in palabra[i])or ("o" in palabra[i])or ("u" in palabra[i]):
            salidav+=palabra[i]
        if not( ("a" in palabra[i]) or ("e" in palabra[i])or ("i" in palabra[i])or ("o" in palabra[i])or ("u" in palabra[i])) and (" " not in palabra[i]):
            salidac+=palabra[i]
    ordenada=salidac+salidav        
    
    return ordenada

print(contar_vocales("curso de programacion"))