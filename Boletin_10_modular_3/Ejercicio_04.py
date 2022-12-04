'''
Diseñe una función llamada numberInString que tenga como parámetro una cadena de caracteres, el
debe devolver cuántos de esos caracteres son números.
'''
def numberInString(string):
    abcdary="0123456789"
    counter=0
    
    for i in range(len(string)):
        if string[i] in abcdary:
            counter+=1
    return counter

print(numberInString("Hola Buenas TARDES, ponme 45 hamburguesas"))
print(numberInString("Me gusta BK mas que MC, BK es un 10 sobre 10"))