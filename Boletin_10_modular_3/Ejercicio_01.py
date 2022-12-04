'''
Diseñe una función llamada charactersInString que tenga como parámetros de entrada una 
cadena de caracteres y un caráctery devuelva el número de veces que ese carácter aparece 
en la cadena.
'''


def charactersInString(c, string):
    count=0
    for i in range(len(string)):
        if c.upper() == string[i].upper():
            count+=1
    return count

print(charactersInString("a", "La vida es un fastidio maravilloso"))