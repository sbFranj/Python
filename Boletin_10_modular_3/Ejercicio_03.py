'''
Diseñe una función llamada upperCaseInString que tenga como parámetro una cadena de caracteres, el
debe devolver cuántos de esos caracteres son mayúsculas.
'''
def upperCaseInString(string):
    abcdary="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    counter=0
    
    for i in range(len(string)):
        if string[i] in abcdary:
            counter+=1
    return counter

print(upperCaseInString("Hola Buenas TARDES"))
print(upperCaseInString("Me gusta BK mas que MC"))