'''
Escribe una función que, dada una lista de caracteres, devuelva la cadena más larga.
Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá la
que tenga el mayor número de caracteres repetidos .
'''

cadena_1="azucar, leche, platano, avena, cacahueteeeeeeeeee55"
cadena_2="cacahuete,aazucar, leche, platano,aavenaasdlkpcnrkk"


def contarLongitud(cadena1, cadena2):
    cadena1      
    if len(cadena1)<len(cadena2):
        cadena1=cadena2
    
    elif len(cadena1)==len(cadena2):
        l1=[]
        l2=[]
        for i in range(len(cadena1)):
            if cadena1[i] not in l1:
                l1.append(cadena1[i])
            if cadena2[i] not in l2:
                l2.append(cadena2[i])
        if len(l1)>len(l2):
            cadena1=cadena2                                    
                
    return cadena1

print(f"es mas larga la cadena: {contarLongitud(cadena_1, cadena_2)}")

