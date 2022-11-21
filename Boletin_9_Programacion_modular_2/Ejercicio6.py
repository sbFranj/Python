'''
Diseñe un método llamado getNumberOfDigits que reciba un número (puede ser
real, entero, positivo o negativo) y que devuelva el número de dígitos que contiene. Si
el parámetro no es válido, el método debe devolver None. Amplíe esta función a
otros sistemas numéricos (hexadecimal, decimal, binario, octal).
'''


digit=int(input("Enter a number: "))
def isBinary(number):
    binario=True
    number=str(number)
    if ("1" not in number) and ("0" not in number):
        binario=False
    return binario

def isDecimal(number):
    decimal=True 
    number=str(number)
    if ("0" not in number) and ("1" not in number)and ("2" not in number)and ("3" not in number)and ("4" not in number)and ("5" not in number)and ("6" not in number)and ("7" not in number)and ("8" not in number)and ("9" not in number):
        decimal=False
    return decimal
    
def getNumberOfDigits(number):
    count=0
    for i in range(len(str(number))):
        count+=1
    return count


print(getNumberOfDigits(digit))
print(isDecimal(digit))
