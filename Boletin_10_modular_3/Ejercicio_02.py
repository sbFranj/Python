'''
Diseñe una función llamada lowCaseInString que tenga como 
parámetro una cadena de caracteres, eldebe devolver cuántos 
de esos caracteres son minúsculas
'''


def lowCaseInString(string):
    abcdary="abcdefghijklmnñopqrstuvwxyz"
    counter=0
    
    for i in range(len(string)):
        if string[i] in abcdary:
            counter+=1
    return counter

print(lowCaseInString("Hola Buenas TARDES"))
print(lowCaseInString("Me gusta BK mas que MC"))















