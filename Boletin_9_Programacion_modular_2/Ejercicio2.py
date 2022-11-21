'''
Diseñe un método llamado isLeapYear que reciba un número y devuelva False para
años comunes y True para los años bisiestos. Puede que sepa que un año se considera
bisiesto si es divisible por 4, a menos que también sea divisible por 100. Un año no es
bisiesto si es divisible por 100, a menos que también sea divisible por 400.
'''


year=int(input("Enter a year: "))

def isLeapYear(number):
    return number%4==0 and (number%100!=0 or number%400==0)

print(isLeapYear(year))